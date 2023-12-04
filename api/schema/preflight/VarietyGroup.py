import graphene

from api.models_choices import LOCATIONS_CHOICES, VARITIES_CHOICES


class VarietyGroupPreflightQuery(graphene.ObjectType):
    """
    Preflight Query for Location Ranking and Variety Comparator operations.

    Represents the preflight query for the `LocationRanking` and `VarietyComparator` operations.
    This operation allows obtaining certain predefined options and other payload.
    """

    class Meta:
        description = __doc__

    campaign_options_list = graphene.List(graphene.String)
    location_options_list = graphene.List(graphene.String)
    variety_options_list = graphene.List(graphene.String)

    def resolve_campaign_options_list(self, info):
        campaign_options = ["not implemented"]
        return campaign_options

    def resolve_location_options_list(self, info):
        location_options = [location[0] for location in LOCATIONS_CHOICES]
        return location_options

    def resolve_variety_options_list(self, info):
        variety_options = [variety[0] for variety in VARITIES_CHOICES]
        return variety_options
