from unittest.mock import patch, mock_open, MagicMock
from pathlib import Path
from recipe.routes.utils.ocr_utils import Gemini
import pytest

# Testing for gemini api
class TestGemini():
    MOCK_PATH_EXISTS = 'pathlib.Path.exists'
    MOCK_PATH_OPEN = 'builtins.open'
    MOCK_DOTENV_VALUES = 'recipe.routes.utils.ocr_utils.dotenv_values'
    MOCK_GENAI_CLIENT = 'recipe.routes.utils.ocr_utils.genai.Client'

    # -- fixtures --

    @pytest.fixture
    def gemini_instance(self):
        return Gemini(content="e\nTES T\nING LEITEUMTINTEGRAL\nnOIS E")

    @pytest.fixture
    def mock_dotenv_apikey(self):
        return {"GEMINI_API_KEY": "test_api_key"}
    
    @pytest.fixture
    def mock_sys_instructions(self):
        return "Test gemini system instructions"

    @pytest.fixture
    def mock_response(self):
        response = MagicMock()
        response.text = "Leite Integral"  # Expected response
        return response

    # -- tests --

    def test_get_dotenv(self, gemini_instance, mock_dotenv_apikey):
        with patch(self.MOCK_PATH_EXISTS, return_value=True), \
             patch(self.MOCK_DOTENV_VALUES, return_value=mock_dotenv_apikey) as mock_dotenv:
            
            result = gemini_instance.get_dotenv()
            assert result == mock_dotenv_apikey
            mock_dotenv.assert_called_once()
    
    def test_get_system_instructions(self, gemini_instance, mock_sys_instructions):
        with patch(self.MOCK_PATH_EXISTS, return_value=True), \
             patch(self.MOCK_PATH_OPEN, mock_open(read_data=mock_sys_instructions)) as mock_file:

            result = gemini_instance.get_system_instructions()
            assert result == mock_sys_instructions

    def test_initialize_gemini(self, gemini_instance, mock_dotenv_apikey):
        with patch.object(gemini_instance, 'get_dotenv', return_value=mock_dotenv_apikey), \
             patch(self.MOCK_GENAI_CLIENT, return_value=MagicMock()) as mock_client:
            
            assert gemini_instance.initialize_gemini() is True
            mock_client.assert_called_once_with(api_key=mock_dotenv_apikey["GEMINI_API_KEY"])
            assert gemini_instance.client is not None

    def test_run_gemini(self, gemini_instance, mock_sys_instructions, mock_response):
        gemini_instance.client = MagicMock()
        gemini_instance.client.models.generate_content.return_value = mock_response

        with patch.object(gemini_instance, 'get_system_instructions', return_value=mock_sys_instructions):

            gemini_instance.run_gemini()
            gemini_instance.client.models.generate_content.assert_called_once()
            _, dict_args = gemini_instance.client.models.generate_content.call_args

            assert dict_args['contents'] == gemini_instance.content
            assert dict_args['config'].system_instruction == mock_sys_instructions
            assert gemini_instance.response == mock_response

    def test_execute(self, gemini_instance, mock_response):
        with patch.object(gemini_instance, 'initialize_gemini', return_value=True), \
             patch.object(gemini_instance, 'run_gemini') as mock_run_gemini:

            gemini_instance.response = mock_response
            result = gemini_instance.execute()

            assert result == mock_response.text
            mock_run_gemini.assert_called_once()
             