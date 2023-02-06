

# class Terrain


"""

Biomes
https://ucmp.berkeley.edu/exhibits/biomes/tundra.php
Sizes:
    Island: 1
    MajorTiles: 7 - a center hex and surrounding ring
    MinorTiles: 7 - a center hex and surrounding ring
    SpecificTiles: 7 - a center hex and surrounding ring
    A total of 1 island, 7 MajorTiles, 49 MinorTiles, 343 SpecificTiles




Theoretical steps
Setup:
    Lat/Lon to figure out average temperature based on global temperature. 
    Island rock type, elevation, and elevation profile

Dynamic:
    Wind and extra abnormal weather patterns?
        Huricanes, jetstream, polar vortexes, wind patterns
    Temperature from season (and other weather paterns) and global adjustments
    From Temperauture (and other weather events) calculate island moisture
    For each MajorTile (Upwind to Downwnind -> East to West, Equator to Poles) calculate an expected rainfall
        Elevation change (exaserbaed from faster el change)
        Based on tree cover -> The more trees, half the rainfall impact
            If rainfall goes down, remove water from the forest to make up half the difference and then remove trees
            If rainfall goes up, remove half the moisture to replenish the forest and then increase trees
        So in general as we move west we expect to see less moisture in the biomes
            As we deforest we reduce the islands resilliance to weather
            If we reforest we can increase the islands resilliance to weather
        So you CAN desertify or marshify your island. IE terriforming
        We dont expect to remove all moisture from the air over the island






For the Island:
    Generalte the Lat/Lon
        General average temperature interpolate
            LAT type
            0-14 Hot
            14-28 Warm
            28-42 Temperate
            42-56 Cool
            56-70 Cold
            Seasonal temperature parabolic away form equator
                Hot No different
                Cold Up to a full range different
        # General rainfall parabolic about the equator
        #     Hot Lots
        #     Cold Minimal
    Based on the Island Lat/Lon, calculate the ave temp then each season has a difference in temperature

For each MajorNode:
    Generate Rock formation type either or both
        Volcanic activity
        Earthquate activity
    Generate major features
        Generate Elevation
            X = 100 maybe
            Tree line is at 1.75X maybe
            Each MajorTile gets a height and a height variance
                Outside tiles from (0 to X)
                Inner tile from (ave of outer to double ave of outer?)
                weight of 100
                height variation is more likely to be quite flat or quite bumpy
            Generate a random elevation maping for the MinorTiles and a height variance
                from -X to X
                weight of 10
                height variance is largely drivin by the varaince in the MajorTile but we want to try to either get large vallies/hills or rather flat terrain
            Generate a random elevation maping for the SpecificTiles
                I forget the equiation, but at low MinorTile height difference from MajorTile, make the specifcTile differences VERY small for flat land
                    if high difference between MinorTile and MajorTile, make differences in SpecificTile larger to make very hilly terrain. We want to drive 
                    either rivers or open marshy terrain in a sort
                from -X to X
                weight of 1
        Going East to West, Equator to Poles
            Calculate Island moisture in air from current temperature at sea level
            For each MajorTile average elevation, calculate temperature change
                Then remove moisture as a result of RH changes
                If there is a sharp elevation change it has an exponential impact on precip
            For each MinorTile and SpecificTile
                Somehow figure out rivers/streams/ponds/lakes etc.
        Trees Percent
            Each MajorTile tree percentage calculation
                From precip calculation before
            Each MinorTile tree percentage calculation
                Take the MajorTile tree percentage and add +- 1/4 of coverage
                    So if the climate is Cool(0-60%) and the % is 40%,
                    the range for the MinorTile will be from 25% to 55%
                    So if the climate is Cool(0-60%) and the % is 50%,
                    the range for the MinorTile will be from 35% to 60% because it cant be over 60
            Each SpecificTile will randomly select between the MinorTile range

        Major river or lakes
            At high elev
            Calculate from low points from the height calculator
            Glacure activity if cold and high rainfall
    Calculate minor features
        Tree percent calculated from rainfall
            type tree percent ranges
            Hot
                0-100%
            Warm
                0-100%
            Temperate
                0-100%
            Cool
                0-60%
            Cold
                0-30%
        Trees Percent Name
            0-10% Prarie
            10-30% Savanah
            30-50% Woods
            50-75% Forest
            75-100% Jungle
        Forest name
            Hot
                Tropical but can be Rain if high rain
            Warm
                Tropical or Temperate
            Temperate
                Temperate
            Cool
                Temperate or Boreal
            Cold
                Boreal but can be Taiga if high rain
        Area between woods
Desert/Tundra
    Sand vs Barin
    Arctic vs Alpine
Grassland
    Temporate vs Tropical
Wetland
    Marsh - no trees
    Swamp - lots of trees
    Bog - very wet
    Fens - a Bog thats not fed from a river


Desert
Flooded
Montane
Tropical
Temperate
Tundra

Floodplanes
Marsh
Swamp

Wetlands
Marsh
    no trees
Swamp
    lots of trees
Bog
    very wet
Fens
    Not fed from a river



            0- Desert
            - Temperate Grassland
            -100 Tropical Grassland


        Woods
        Forest
        Jungle
        Planes
        Grassland
        Tundra
        Desert

    Calculate expected weather and tweaks
        From East to West cascade rainfall and temperature to drive these:
            Woods are small and dense
            forest large
            jungle overgrown

            forest
                trees and undergrowth
                rain forest, tropical forest, boreal forest, temperate forest
            woods
                just a smaller area than a forest
            jungle
                overgrown with exotic things and tangle dvegitation
                lots of plants along the ground

            grassland:
                prarie savanah
                They are next to eachother as the area dictates
            prarie
                have no trees (less than 10% trees)
            savanna
                Has some trees (less than 30% trees)
            



    











Have a large number of hex terrain nodes

Master Node
    Lat/Lon
    General Temperature
        North/South temperature
    Fish in the area
        Migrational animals


Have a few Major Nodes
    6 to determine things such as

        Based on the location of the tile and things like the temperature of the island and thus the water around it

        Rock formation type
        Earthquake Activity
        Volcanic Activity

        Mountains
        Major Rivers
        Aquaduct
        Plateaus
        Mesas

        Caves




        Forrest
        Jungle
        Mountains
        Hills
        Major Rivers
        Earthquate zone
        Caves
        Aquaduct
        Underground minerals
        Plateaus
            volcanic, tectonic
        Mesas
        Valleys
        Basins
        Wetlands
        Temperature based on the initial temperature and lat/lon
        



        Grassland
        Planes
        Desert
        Tundra
        Snow
        Ice
        Woods
        Rainforest
        Marsh
        Flodplanes
        Oasis
        Cliff
        Volcano
        Geothermal Fissures


        Ocea
        Coast
        Reef

        Rock formation type
        Elevation


Have quote a few Minor Nodes
    The ones along the edge are special. Between Major Nodes
        and connected to the ocean for things like ithmises
        islands etc
Have a large number of Specific Nodes

"""

class Client:
    def __init__(self):
        self.id = None
        self.name = None
        self.description = None
        self.population = None
        self.notes = None
        self.changelog = None
        self.history = None

    @property
    def put(self):
        x=1

    @classmethod
    def build(self, dct):
        x=1

    @classmethod
    def load(self, id):
        x=1


