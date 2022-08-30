import sdRDM

from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional


@forge_signature
class Dataset(sdRDM.DataModel):

    """..."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("datasetINDEX"),
    )
    name: Optional[str] = Field(
        description="Name of the experimentator.",
        default=None,
    )

    compound: Optional[str] = Field(
        description="Name of the compound.",
        default=None,
    )

    spec_information: Optional[str] = Field(
        description="Information about the spectrometer.",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/example_showcase.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="8616086697bd98fa32c63145943156e8935b007c"
    )
