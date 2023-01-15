
# ‎

<style type="text/css">
p {
   margin: 2px 0;
}
</style>

<p style="width:70%; font-size:40px; text-align:left; color:#757575">Publications</p>


```{dropdown} <p style="font-size:16px; font-family:Arial, sans-serif;">Nonclassical Nucleation of Zinc Oxide from a Physically Motivated Machine-Learning Approach</p> <p style="font-size:14px;font-family:Arial, sans-serif;"> J. Goniakowski, S. Menon, G. Laurens, and J. Lam </p> <a href=https://doi.org/10.1021/acs.jpcc.2c06341 style="font-size:12px">The Journal of Physical Chemistry C (126) 40, 2022 </a> 

Observing nonclassical nucleation pathways remains challenging in simulations of complex materials with technological interests. This is because it requires very accurate force fields that can capture the whole complexity of their underlying interatomic interactions and an advanced structural analysis able to discriminate between competing crystalline phases. Here, we first report the construction and particularly thorough validation of a machine-learning force field for zinc oxide interactions using the Physical LassoLars Interaction Potentials approach which allows us to be predictive even for high-temperature dynamical systems such as ZnO melt. Then, we carried out several types of crystallization simulations and followed the formation of ZnO crystals with atomistic precision. Our results, which were analyzed using a data-driven approach based on bond order parameters, demonstrate the presence of both prenucleation clusters and two-step nucleation scenarios, thus retrieving seminal predictions of nonclassical nucleation pathways made on much simpler models. Dedicated calculations of high-temperature ZnO free energy within a newly developed automated nonequilibrium thermodynamic integration method revealed the existence of a thermodynamic bias for the predicted nonclassical nucleation scenarios.

[Read more..](https://pubs.acs.org/doi/pdf/10.1021/acs.jpcc.2c06341)
```

```{dropdown} <p style="font-size:16px; font-family:Arial, sans-serif;">Efficient parametrization of the atomic cluster expansion</p> <p style="font-size:14px;font-family:Arial, sans-serif;"> A. Bochkarev, Y. Lysogorskiy, S. Menon, M. Qamar, M. Mrovec, and R. Drautz </p> <a href=https://doi.org/10.1103/physrevmaterials.6.013804 style="font-size:12px">Physical Review Materials (6) 1, 2022 </a> 

The atomic cluster expansion (ACE) provides a general, local, and complete representation of atomic energies. Here we present an efficient framework for parametrization of ACE models for elements, alloys, and molecules. To this end, we first introduce general requirements for a physically meaningful description of the atomic interaction, in addition to the usual equivariance requirements. We then demonstrate that ACE can be converged systematically with respect to two fundamental characteristics—the number and complexity of basis functions and the choice of nonlinear representation. The construction of ACE parametrizations is illustrated for several representative examples with different bond chemistries, including metallic copper, covalent carbon, and several multicomponent molecular and alloy systems. We discuss the Pareto front of optimal force to energy matching contributions in the loss function, the influence of regularization, the importance of consistent and reliable reference data, and the necessity of unbiased validation. Our ACE parametrization strategy is implemented in the freely available software package pacemaker that enables largely automated and GPU accelerated training. The resulting ACE models are shown to be superior or comparable to the best currently available ML potentials and can be readily used in large-scale atomistic simulations.

[Read more..](https://doi.org/10.1103/physrevmaterials.6.013804)
```

```{dropdown} <p style="font-size:16px; font-family:Arial, sans-serif;">Automated free-energy calculation from atomistic simulations</p> <p style="font-size:14px;font-family:Arial, sans-serif;"> S. Menon, Y. Lysogorskiy, J. Rogal, and R. Drautz </p> <a href=https://doi.org/10.1103/physrevmaterials.5.103801 style="font-size:12px">Physical Review Materials (10) 1, 2022 </a> 

We devise automated workflows for the calculation of Helmholtz and Gibbs free energies and their temperature and pressure dependence and provide the corresponding computational tools. We employ nonequilibrium thermodynamics for evaluating the free energy of solid and liquid phases at a given temperature and reversible scaling for computing free energies over a wide range of temperatures, including the direct integration of P-T coexistence lines. By changing the chemistry and the interatomic potential, alchemical and upscaling free energy calculations are possible. Several examples illustrate the accuracy and efficiency of our implementation.

[Read more..](https://doi.org/10.1103/physrevmaterials.5.103801)
```

```{dropdown} <p style="font-size:16px; font-family:Arial, sans-serif;">Nucleation and growth during solidification in metals and alloys</p> <p style="font-size:14px;font-family:Arial, sans-serif;"> S. Menon </p> <a href=https://doi.org/10.13154/294-8488 style="font-size:12px">Doctoral thesis, Ruhr-University Bochum, 2022 </a> 

Nucleation during solidification is a fundamental phenomenon in nature. Understanding the process on an atomic scale is necessary as the early stages of nucleation significantly impact the microstructure of a material. In this thesis, atomistic simulations are employed to study nucleation in metals and alloys. In bcc metals, a non-classical nucleation mechanism consisting of two steps was observed: the formation of a pre-structured region of high crystalline order in the supercooled liquid, followed by the emergence of the crystalline bulk phase within. The pre-structured region plays a crucial role in the nucleation process as it provides a diffusive interface between crystalline and liquid phases, providing a region of low interfacial energy. Furthermore, the structural features of pre-ordering indicate the precursors for the formation of the crystalline bcc phase, elucidating its role in polymorph selection.
An investigation into the thermodynamic aspects of nucleation reveals that the energy barrier in the early stages is dominated by entropic contributions, which leads to pre-ordering. The inherent similarity in the nucleation mechanism observed in bcc metals with that of metals that exhibit different crystalline states indicates that
the formation of a pre-ordered phase is a general feature observed in these materials.

Furthermore, the nucleation mechanism in a binary metal-semiconductor alloy is investigated. The nucleation mechanism is concentration-dependent, characterised by the competition between crystallisation and phase separation in the liquid.
At low concentrations of the semiconductor phase, only nucleation into a closepacked crystalline structure is observed. The free energy barrier for nucleation increases with concentration. Thus, a local reduction in concentration, leading to
pre-structuring in liquid, is necessary for crystallisation. At eutectic concentration and beyond, nucleation is preceded by phase separation in the liquid. The formation of pre-structuring is observed to be an essential initial step at all concentrations. Pre-ordering in alloys performs the dual function of providing a region of both bond-orientational order and density matching the bulk crystalline phase, paving the way for crystallisation. This thesis provides a comprehensive insight into the nucleation mechanism in bcc metals and metal-semiconductor alloys from an atomistic
perspective, focusing on pre-ordering, the initial stage of nucleation, and can aid in the understanding and interpretation of experimental studies of nucleation. Furthermore, controlling the pre-ordered phase through methods such as seeding or environmental conditions could help control the formation of the bulk crystalline phase, and in turn, material properties.

[Read more..](https://doi.org/10.13154/294-8488)
```

```{dropdown} <p style="font-size:16px; font-family:Arial, sans-serif;">Performant implementation of the atomic cluster expansion PACE and application to copper and silicon</p> <p style="font-size:14px;font-family:Arial, sans-serif;"> Y. Lysogorskiy, C. van der Oord, A. Bochkarev, S. Menon, M. Rinaldi, T. Hammerschmidt, M. Mrovec, A. Thompson, Gabor Csanyi, C. Ortner, and R. Drautz </p> <a href=https://doi.org/10.1038/s41524-021-00559-9 style="font-size:12px">npj Computational Materials (7) 1, 2021 </a> 

The atomic cluster expansion is a general polynomial expansion of the atomic energy in multi-atom basis functions. Here we implement the atomic cluster expansion in the performant C++ code PACE that is suitable for use in large-scale atomistic simulations. We briefly review the atomic cluster expansion and give detailed expressions for energies and forces as well as efficient algorithms for their evaluation. We demonstrate that the atomic cluster expansion as implemented in PACE shifts a previously established Pareto front for machine learning interatomic potentials toward faster and more accurate calculations. Moreover, general purpose parameterizations are presented for copper and silicon and evaluated in detail. We show that the Cu and Si potentials significantly improve on the best available potentials for highly accurate large-scale atomistic simulations.

[Read more..](https://doi.org/10.1038/s41524-021-00559-9)
```

```{dropdown} <p style="font-size:16px; font-family:Arial, sans-serif;">Role of pre-ordered liquid in the selection mechanism of crystal polymorphs during nucleation</p> <p style="font-size:14px;font-family:Arial, sans-serif;"> S. Menon, G. Diaz Leines, R. Drautz, and J. Rogal </p> <a href=https://doi.org/10.1063/5.0017575 style="font-size:12px">The Journal of Chemical Physics (153) 10, 2020 </a> 

We investigate the atomistic mechanism of homogeneous nucleation during solidification in molybdenum employing transition path sampling. The mechanism is characterized by the formation of a pre-structured region of high bond-orientational order in the supercooled liquid followed by the emergence of the crystalline bulk phase within the center of the growing solid cluster. This precursor plays a crucial role in the process as it provides a diffusive interface between the liquid and crystalline core, which lowers the interfacial free energy and facilitates the formation of the bulk phase. Furthermore, the structural features of the pre-ordered regions are distinct from the liquid and solid phases and preselect the specific polymorph that nucleates. The similarity in the nucleation mechanism of Mo with that of metals that exhibit different crystalline bulk phases indicates that the formation of a precursor is a general feature observed in these materials. The strong influence of the structural characteristics of the precursors on the final crystalline bulk phase demonstrates that for the investigated system, polymorph selection takes place in the very early stages of nucleation.

[Read more..](https://doi.org/10.1063/5.0017575)
```

```{dropdown} <p style="font-size:16px; font-family:Arial, sans-serif;">pyscal: A python module for structural analysis of atomic environments</p> <p style="font-size:14px;font-family:Arial, sans-serif;"> S. Menon, G. Diaz Leines, and J. Rogal </p> <a href=https://doi.org/10.21105/joss.01824 style="font-size:12px">Journal of Open Source Software (4) 43, 2019 </a> 

pyscal is a python module for the calculation of local atomic structural environments including Steinhardt’s bond orientational order parameters during post-processing of atomistic simulation data. The core functionality of pyscal is written in C++ with python wrappers using pybind11 which allows for fast calculations with possibilities for easy expansion in python.

[Read more..](https://doi.org/10.21105/joss.01824)
```


