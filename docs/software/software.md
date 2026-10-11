# Software

:::::{tab-set}

::::{tab-item} MLIPs & thermodynamics

:::{card} GRACE
:class-card: item-card

GRACE (Graph Atomic Cluster Expansion) extends ACE to multi-component materials and graph architectures, with foundation models covering a broad range of chemistries. The gracemaker package handles fitting, uncertainty estimates, and export to LAMMPS, including the Kokkos pair styles.
+++
[Repository](https://github.com/ICAMS/grace-tensorpotential) &nbsp;|&nbsp; [Docs](https://gracemaker.readthedocs.io/) &nbsp;|&nbsp; [Foundation models](https://huggingface.co/AMS-ICAMS-RUB/grace-foundation-models) &nbsp;|&nbsp; [Publication](https://doi.org/10.1103/PhysRevX.14.021036)
:::

:::{card} calphy
:class-card: item-card

<img src="https://calphy.org/_static/calphy_logo.png" class="sw-logo" alt="calphy logo">

calphy is a Python library and command line interface for free energy calculations. calphy provides fully automated routines for calculation of free energy using interatomic potentials, which in turn can be used to calculate complex thermodynamic properties such as melting temperature, specific heat and phase diagrams.
+++
[Repository](https://github.com/ICAMS/calphy) &nbsp;|&nbsp; [Docs](https://calphy.org/) &nbsp;|&nbsp; [Publication](https://doi.org/10.1103/PhysRevMaterials.5.103801)
:::

:::{card} pace
:class-card: item-card

PACE is the performant C++ implementation of the Atomic Cluster Expansion method suitable for large scale atomic simulations using LAMMPS.
+++
[Repository](https://github.com/ICAMS/lammps-user-pace) &nbsp;|&nbsp; [Publication](https://doi.org/10.1038/s41524-021-00559-9)
:::

:::{card} pylammpsmpi
:class-card: item-card

<img src="https://avatars.githubusercontent.com/u/25691954?s=200&v=4" class="sw-logo" alt="pyiron logo">

pylammpsmpi is a python module which enables using the atomistic simulation code LAMMPS from jupyter notebooks in a parallel environment. pylammpsmpi can also be deployed on queueing systems.
+++
[Repository](https://github.com/pyiron/pylammpsmpi) &nbsp;|&nbsp; [Docs](https://pylammpsmpi.readthedocs.io/en/latest/) &nbsp;|&nbsp; [Zenodo](https://doi.org/10.5281/zenodo.5034216)
:::

::::

::::{tab-item} Structure analysis

:::{card} pyscal
:class-card: item-card

<img src="https://pyscal.org/en/latest/_images/pyscal_v2_logo_1.png" class="sw-logo" alt="pyscal logo">

pyscal is a python module for the calculation of local atomic structural environments including Steinhardt’s bond orientational order parameters during post-processing of atomistic simulation data. The core functionality of pyscal is written in C++ with python wrappers using pybind11 which allows for fast calculations with possibilities for easy expansion in python.
+++
[Repository](https://github.com/pyscal/pyscal) &nbsp;|&nbsp; [Docs](https://pyscal.org/en/latest/index.html) &nbsp;|&nbsp; [Publication](https://joss.theoj.org/papers/10.21105/joss.01824) &nbsp;|&nbsp; [Zenodo](https://doi.org/10.5281/zenodo.3522376)
:::

:::{card} pyscal3
:class-card: item-card

<img src="https://pyscal.org/en/latest/_images/pyscal_v3_logo_1.png" class="sw-logo" alt="pyscal3 logo">

pyscal3 is a more robust, and even faster implementation of the original pyscal code. It is a step towards pyscal being a code not just for local structural environment, but for complete atomic structure manipulation. pyscal3 is memory efficient and can handle tens of thousands of atoms. It is currently under development.
+++
[Repository](https://github.com/pyscal/pyscal3) &nbsp;|&nbsp; [Docs](https://v3.pyscal.org/en/latest/)
:::

::::

::::{tab-item} Knowledge graphs

:::{card} atomRDF
:class-card: item-card

<img src="https://atomrdf.pyscal.org/en/latest/_static/logo.png" class="sw-logo" alt="atomRDF logo">

atomRDF is a python tool for ontology-based creation, manipulation, and querying of structures. atomRDF is powered by the Computational Material Sample Ontology (CMSO) and pyscal3. The package is currently under active development.
+++
[Repository](https://github.com/pyscal/atomrdf) &nbsp;|&nbsp; [Docs](https://rdf.pyscal.org/en/latest/) &nbsp;|&nbsp; [Ontology](https://github.com/Materials-Data-Science-and-Informatics/cmso-ontology) &nbsp;|&nbsp; [Zenodo](https://doi.org/10.5281/zenodo.8146527)
:::

:::{card} tools4RDF
:class-card: item-card

tools4RDF is a python toolkit for working with RDF data, providing utilities for building, querying, and visualising knowledge graphs of materials science data. It complements atomRDF and powers downstream tooling such as the atomkg.pyscal.org portal.
+++
[Repository](https://github.com/OCDO/tools4RDF) &nbsp;|&nbsp; [Docs](https://tools4rdf.readthedocs.io/en/latest/) &nbsp;|&nbsp; [Publication](https://doi.org/10.21105/joss.09482)
:::

:::{card} atomkg.pyscal.org
:class-card: item-card

A deployed interactive knowledge-graph portal for computational materials science data, featuring force-directed visualisation, composition-based filtering, and an experimental LLM-driven natural-language to SPARQL interface (powered by Groq and tools4RDF) for agentic exploration of simulation data.
+++
[Live site](https://atomkg.pyscal.org/) &nbsp;|&nbsp; [Methodology preprint](https://arxiv.org/abs/2604.06230)
:::

::::

:::::
