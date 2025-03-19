"""Supported file formats and their MIME types."""

from enum import StrEnum, auto


class SupportedFileFormats(StrEnum):
    """Supported file formats."""

    TXT = auto()
    DOC = auto()
    DOCX = auto()
    PDF = auto()
    EPUB = auto()
    PPT = auto()
    PPTX = auto()


class MIMETypes(StrEnum):
    """MIME types for the supported file formats."""

    TXT = "text/plain"
    DOC = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    DOCX = "application/msword"
    PDF = "application/pdf"
    EPUB = "application/epub"
    PPT = "application/ppt"
    PPTX = "application/pptx"


type_of_file = {
    SupportedFileFormats.TXT: MIMETypes.TXT,
    SupportedFileFormats.DOC: MIMETypes.DOC,
    SupportedFileFormats.DOCX: MIMETypes.DOCX,
    SupportedFileFormats.PDF: MIMETypes.PDF,
    SupportedFileFormats.EPUB: MIMETypes.EPUB,
    SupportedFileFormats.PPT: MIMETypes.PPT,
    SupportedFileFormats.PPTX: MIMETypes.PPTX,
}
