from contextlib import ExitStack
from pathlib import Path

from langchain.document_loaders import (
    UnstructuredAPIFileIOLoader,
    UnstructuredAPIFileLoader,
)


def test_unstructured_api_file_loader() -> None:
    """Test unstructured loader."""
    file_path = str(Path(__file__).parent.parent / "examples/layout-parser-paper.pdf")
    loader = UnstructuredAPIFileLoader(
        file_path=file_path,
        api_key="FAKE_API_KEY",
        strategy="fast",
        mode="elements",
    )
    docs = loader.load()

    assert len(docs) > 1


def test_unstructured_api_file_loader_multiple_files() -> None:
    """Test unstructured loader."""
    file_paths = [
        str(Path(__file__).parent.parent / "examples/layout-parser-paper.pdf"),
        str(Path(__file__).parent.parent / "examples/whatsapp_chat.txt"),
    ]

    loader = UnstructuredAPIFileLoader(
        file_paths=file_paths,
        api_key="FAKE_API_KEY",
        strategy="fast",
        mode="elements",
    )
    docs = loader.load()

    assert len(docs) > 1


def test_unstructured_api_file_io_loader() -> None:
    """Test unstructured loader."""
    file_path = str(Path(__file__).parent.parent / "examples/layout-parser-paper.pdf")

    with open(file_path, "rb") as f:
        loader = UnstructuredAPIFileIOLoader(
            file=f,
            file_filename=file_path,
            api_key="FAKE_API_KEY",
            strategy="fast",
            mode="elements",
        )
        docs = loader.load()

    assert len(docs) > 1


def test_unstructured_api_file_loader_io_multiple_files() -> None:
    """Test unstructured loader."""
    file_paths = [
        str(Path(__file__).parent.parent / "examples/layout-parser-paper.pdf"),
        str(Path(__file__).parent.parent / "examples/whatsapp_chat.txt"),
    ]

    with ExitStack() as stack:
        files = [stack.enter_context(open(file_path, "rb")) for file_path in file_paths]

        loader = UnstructuredAPIFileIOLoader(
            files=files,  # type: ignore
            file_filenames=file_paths,
            api_key="FAKE_API_KEY",
            strategy="fast",
            mode="elements",
        )

        docs = loader.load()

    assert len(docs) > 1