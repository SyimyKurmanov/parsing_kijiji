from configs.a import RequestTranslator


class Paginator(RequestTranslator):
    def find_button_next(self) -> bool:
        """
        показывает, имеется ли кнопка next на странице
        """
        pagination = self._get_soup().find('div', class_='pagination')
        return 'Next' in pagination.text

