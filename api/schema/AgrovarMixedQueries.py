from api.schema.common.CampaignPaper import CampaignPaperQuery
from api.schema.preflight.VarietyGroup import VarietyGroupPreflightQuery


class AgrovarMixedQueries(CampaignPaperQuery, VarietyGroupPreflightQuery):
    """
    Main global query mixing for all Agrovar API Endpoints.
    """

    class Meta:
        description = __doc__
