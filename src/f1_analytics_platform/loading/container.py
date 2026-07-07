from f1_analytics_platform.loading.database import F1Database


class LoadingContainer:
    def __init__(self):
        self._f1_db = F1Database()

    @property
    def f1_db(self) -> F1Database:
        return self._f1_db
