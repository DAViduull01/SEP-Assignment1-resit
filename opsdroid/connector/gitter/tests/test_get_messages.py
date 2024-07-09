import unittest
from unittest.mock import AsyncMock, patch, MagicMock
import asyncio
from opsdroid.connector.gitter import ConnectorGitter

def async_iter(iterable):
    """Helper to create an async iterator from an iterable."""
    async def async_gen():
        for item in iterable:
            yield item
    return async_gen()

class TestMyClass(unittest.IsolatedAsyncioTestCase):
    
    async def asyncSetUp(self):
        self.mock_response = MagicMock()
        self.mock_response.content.iter_chunked = MagicMock(return_value=async_iter([b'message_chunk']))
        
        self.mock_opsdroid = AsyncMock()
        
        self.my_class_instance = ConnectorGitter({})
        self.my_class_instance.response = self.mock_response
        self.my_class_instance.opsdroid = self.mock_opsdroid
        self.my_class_instance.update_interval = 1
        self.my_class_instance.bot_gitter_id = "bot_id"
        self.my_class_instance.parse_message = AsyncMock(return_value=None)

    @patch('asyncio.sleep', new_callable=AsyncMock)
    async def test_get_messages(self, mock_sleep):
        await self.my_class_instance._get_messages()
        
        # Check that sleep was called with the correct interval
        mock_sleep.assert_called_once_with(1)

        # Check that iter_chunked was called
        self.mock_response.content.iter_chunked.assert_called_once_with(1024)

        # Check that parse_message was called with the chunked data
        self.my_class_instance.parse_message.assert_awaited_once_with(b'message_chunk')

        # Since parse_message returns None, opsdroid.parse should not be called
        self.mock_opsdroid.parse.assert_not_called()
    
    @patch('asyncio.sleep', new_callable=AsyncMock)
    async def test_get_messages_with_valid_message(self, mock_sleep):
        valid_message = MagicMock()
        valid_message.user_id = "other_user_id"
        self.my_class_instance.parse_message = AsyncMock(return_value=valid_message)
        
        await self.my_class_instance._get_messages()
        
        self.my_class_instance.parse_message.assert_awaited_once_with(b'message_chunk')
        self.mock_opsdroid.parse.assert_awaited_once_with(valid_message)
    
    @patch('asyncio.sleep', new_callable=AsyncMock)
    async def test_get_messages_with_bot_message(self, mock_sleep):
        bot_message = MagicMock()
        bot_message.user_id = "bot_id"
        self.my_class_instance.parse_message = AsyncMock(return_value=bot_message)
        
        await self.my_class_instance._get_messages()
        
        self.my_class_instance.parse_message.assert_awaited_once_with(b'message_chunk')
        self.mock_opsdroid.parse.assert_not_called()

if __name__ == "_main_":
    unittest.main()