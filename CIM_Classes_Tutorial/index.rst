.. CIMantic Graphs

================================================
CIM Classes Tutorial
================================================

This tutorial provides an overview of usage of the UCAiug Common Information Model (CIM) and mappings to the IEC 61970, 61968, and 62325 standards for modeling power systems equipment, assets, and markets.

The CIM is freely available to use and extend. The CIM is maintained by the UCAiug (informally known as the CIM User’s Group) under an Apache 2.0 license. The CIM Users Group collaborates with the IEC and other standards communities for the development of technical and informative specifications. Although portions of the information model are referred to by the corresponding IEC standards naming, it is not necessary to purchase any of the IEC standards to use the CIM information model.

The latest version of CIM information model (CIM17v40 and draft CIM18v10) can be downloaded from the [UCAiug Website](https://cimug.ucaiug.org/CIM%20Model%20Releases/Forms/AllItems.aspx).

This tutorial provides python-based examples serving as a first introduction to CIM for utility engineers, power systems researchers, and application developers, providing a broad view of the CIM and how particular profiles can be adapted for various use cases. 

The tutorial is also available as a set of executable iPython / Jupyter notebooks on the [PNNL-CIM-Tools GitHub]()

Additional resources explaing the *why* an information model like CIM is needed as well as *what* are described by the classes and attributes are available as a set of citable technical reports available online.


* [Enabling Data Exchange and Data Integration with the Common Information Model, https://doi.org/10.2172/1922947](https://doi.org/10.2172/1922947)

* [A Power Application Developer's Guide to the Common Information Model, https://doi.org/10.2172/2007843](https://doi.org/10.2172/2007843)


All examples are based on usage of the open-source CIMantic Graphs python library developed by Pacific Northwest National Laboratory (PNNL) with support of US Dept of Energy Office of Electricity.

CIMantic Graphs is an open-source library for for creating, parsing, and editing CIM power system models using in-memory knowledge graphs to reduce the burden and learning curve associated with using CIM.

To install CIMantic Graphs, clone the github repository or use pip install: `pip install cim-graph`


.. toctree::
   :caption: Overview
   :maxdepth: 2

   01_understanding_uml
   02_identifiers_naming
   03_equipment_containers
   04_nodes_terminals
