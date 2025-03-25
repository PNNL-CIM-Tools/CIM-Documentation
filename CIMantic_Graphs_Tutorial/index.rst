.. CIMantic Graphs

================================================
CIMantic Graphs Library Documentation
================================================

Python library for creating in-memory labeled property graphs for creating, parsing, and editing CIM power system models. It creates Python object instances in memory using a data profile exported from a specified CIM profile (e.g. IEC61970cim18v01 or GridAPPS-D CIM100 RC4_2021).

The library is being expanded to cover centralized applications, transmission models, and real-time editing of CIM XML models natively.

To install CIMantic Graphs clone the github repository or use pip install: pip install cim-graph

.. image:: CIM_Graph_Logo.png


.. toctree::
   :caption: Overview
   :maxdepth: 2

   01_overview/1_1_overview
   01_overview/1_2_installation
   01_overview/1_3_structure
   01_overview/1_4_contributing

.. toctree::
   :caption: CIM Profiles
   :maxdepth: 2

   02_cim_profiles/2_1_profiles_overview
   02_cim_profiles/2_2_building_profiles
   02_cim_profiles/2_3_using_objects

.. toctree::
   :caption: Databases
   :maxdepth: 2
   03_databases/3_1_databases_overview
   03_databases/3_2_env_variables
   03_databases/3_3_blazegraph
   03_databases/3_4_neo4j
   03_databases/3_5_graphdb
   03_databases/3_6_mysql
   03_databases/3_7_gridappsd
   03_databases/3_8_xml_file_parser

.. toctree::
   :caption: Graph Models
   :maxdepth: 2
   04_graph_models/4_1_graph_models
   04_graph_models/4_2_feeder_model
   04_graph_models/4_3_node_breaker
   04_graph_models/4_4_bus_branch
   04_graph_models/4_5_distributed_area

.. toctree::
   :caption: Utils Shortcuts
   :maxdepth: 2
   05_utils/5_1_file_writers
   05_utils/5_2_get_all_data
   05_utils/5_3_mermaid



