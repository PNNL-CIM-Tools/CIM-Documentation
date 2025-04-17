.. CIM-Builder

================================================
CIM-Builder Documentation
================================================

CIM-Builder is a new python library developed under the Grid Atlas and MAPLE LEAF projects for creating CIM models "from scratch" with no pre-existing model files. This is a significantly different capability than all other tooling, which requires a source file from which to start, such as OpenDSS, PSSE, or GIS data. The library currently inlcudes three main functionalities:

# automatic creation of new node-breaker substations in CIM based on interactive API calls.

# automatic insertion of existing distribution feeders in CIM into new node-breaker substations.

# automatic insertion of new aggregate feeder data in existing CIM transmission models.


.. toctree::
   :caption: Overview
   :maxdepth: 2

   1_1_overview
   1_2_installation
   1_3_structure
   1_4_contributing

.. toctree::
   :caption: Object Builder
   :maxdepth: 2

   2_1_object_builder
   2_2_one_terminal_object
   2_3_two_terminal_object
   
   :caption: Substation Builder
   :maxdepth: 2

   3_1_single_bus
   3_2_sectionalized_bus

