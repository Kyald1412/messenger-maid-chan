# -*- coding: utf-8 -*-
import logging
from chatterbot import ChatBot
from langdetect import detect


class ChatBotDriver(object):
    def __init__(self):
        self.chatbot = ChatBot(
            'Maid-chan',
            trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
            output_adapter="chatterbot.output.OutputFormatAdapter",
            output_format='text'
        )
        logging.info("Chatterbot is initialized!")

    def get_response_from_chatbot(self, query, language):
        if language not in ['en', 'id', 'tl']:
            return "nyaa <3"
        else:
            if language in ['id', 'tl']:
                self.chatbot.train("chatterbot.corpus.indonesia")
            else:
                self.chatbot.train("chatterbot.corpus.english")
            return self.chatbot.get_response(query)

    def get_response(self, query):
        probable_language = detect(query)
        return self.get_response_from_chatbot(query, probable_language)
