from f1_analytics_platform.extraction.container import ExtractionContainer
from f1_analytics_platform.loading.container import LoadingContainer


class ApplicationContainer:
    def __init__(self):
        self._extraction_container = ExtractionContainer()
        self._loading_container = LoadingContainer()

    @property
    def extraction_container(self) -> ExtractionContainer:
        return self._extraction_container

    @property
    def loading_container(self) -> LoadingContainer:
        return self._loading_container
