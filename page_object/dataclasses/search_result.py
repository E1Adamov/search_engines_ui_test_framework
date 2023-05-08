import dataclasses


@dataclasses.dataclass
class SearchResult:
    """
    This is a structure for storing search engines parsed search results
    """
    title: str
    description: str
