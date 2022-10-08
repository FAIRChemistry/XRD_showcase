import sdRDM

from typing import Optional
from typing import List
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class SpecInf(sdRDM.DataModel):
    """Information about the spectrometer."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("specinfINDEX"),
        xml="@id",
    )

    wl_ratio: Optional[float] = Field(description="...", default=None)

    steptime: Optional[float] = Field(description="Steptime in ...", default=None)

    wl: List[float] = Field(
        description="Different wavelengths of the X-ray.", default_factory=ListPlus
    )

    anode: Optional[str] = Field(description="Material of the anode.", default=None)

    stepsize: Optional[float] = Field(description="Stepsize in degree.", default=None)

    start: Optional[float] = Field(
        description="Starting angle in degrees.", default=None
    )

    theta: Optional[float] = Field(description="Theta.", default=None)

    theta2: Optional[float] = Field(description="TwoTheta.", default=None)

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/XRD_showcase.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="a6fa5ed92b56a8d67074f6f8a1d4d3fcca476f94"
    )
