#!/usr/bin/env python
# coding: utf-8

# In[1]:


# get_ipython().system('pip install openai langchain faiss-cpu')


# # In[2]:


# get_ipython().system('pip install tiktoken')


# # In[3]:


# get_ipython().system('pip install anvil-uplink')


# # In[4]:


# import anvil.server


# In[5]:


#@title Text
text_model_input = """Basis of the plant design
Plant design is an important part of the planning of industrial plants and is
guiding the entire project planning.
The basics of plant design are composed of the project input data, the project sequence and the plant philosophy.
1.1 Project input data
During the course of the project, a great deal of information comes together, which is then incorporated into
must be processed during plant design. This information can be divided into three categories:
 Project design data
 Manufacturer data
 Internally generated data
Project design data is summarized in the design base1 and serves as a
Basis for planning. Typical information is the geographical location, laws,
Standards and the capacity of the plant.
Manufacturer data can basically be divided into two main categories:
in the data resulting from the procurement of bulk materials, the so-called Bulk Material
(e.g. pipes, fittings, etc.) and data for individual equipment (e.g. pumps, vessels,
control valves, etc.). This information flows e.g. into the planning of the plant
and/or serve as test documents for the planning disciplines, the customer, the Be1 Design basis D specification, see section 4.1.
© Springer-Verlag GmbH Germany, part of Springer Nature 2018 1
K. G. Topole, Fundamentals of Plant Design, https://doi.org/10.1007/978-3-662-57418-8_1
2 1 Basis of the plant design
authorities, NOBO2 or PE3. The timely provision of manufacturer data and the checking of the
of this data has a direct influence on the planning process.
Internally generated data: This planning data is used by all planning disciplines
genized. For example, site and installation planning determines the position and orientation of apparatus and structures, which are then detailed by construction planning.
These data are compared with manufacturer data and supplemented.
1.2 Project flow engineering
Engineering can be divided into three main phases. The conceptual phase, the
during the proposal phase of a project with definition of the project runs, the basic phase and the detailed phase.
1.2.1 Basic engineering
Basic engineering is usually the first planning phase after the order has been placed with
a plant engineer and may be based on a Process Engineering Package (PEP) from a licensor or a concept and investment study from an operator.
Deeper aspects of basic engineering especially from a process engineering point of view
view are described again in chap. 4.
Typically, the following design services are provided in Basic Engineering:
 Design and calculation of all process engineering components
 Supplementary process description
 Material Balances
 PFD4, PID5
 Operating concept and maintenance concepts
 Equipment lists and specifications
 Plot and layout plans
 Pipe classes
 Task for the construction planning
 Creation of level 2 schedules
 Cost estimate
2 NOBO D Notified Body, e.g. DEKRA, TÜV. 3 PE D Professional Engineers, who perform testing tasks in the USA, among other things. 4 PFD D Process Flow Diagram, see section 4.6. 5 PID D Pipe and Instrument Diagram,
s. Section 4.10.
1.2 Project sequence Engineering 3
At the end of basic engineering, a so-called authority engineering/approval procedure follows, in which the plant operator obtains an official permit.
The basis of such a procedure with the authorities are PFDs and a procedure description.
Especially in the case of permits under the Federal Immission Control Act or in the
USA after the so-called air-permit, many requirements from environmental law are necessary. The many permits, authorizations and approvals are often separate
to be applied for. The public law requirements may also have to be met in advance.
be examined and investigated whether for the planned project at the intended location
the approvability exists at all.
1.2.2 Front End Engineering Design
Front End Engineering Design (FEED) is a complementary planning step when.
the project does not go directly into the detailed planning phase. The main task of the FEED is to
Reviewing and completing the Basic Engineering design documents:
 Completing the data sheets for machines and apparatuses
 thermal design of heat exchangers
 Create request specifications for equipment with long lead times
 Addition of process and utility PID
 Completing plot and layout plans
 Generate hazard zone plans
 Schedule detailing
 Hourly calculation for all disciplines
1.2.3 Detail Engineering
Detail Engineering is the continuation of Basic Engineering or FEED and is used to
to provide all services to ultimately build a plant. That is, in the
Detail Engineering the actual construction, assembly and design documents are
created.
More in-depth aspects of detail engineering, especially from a process engineering point of view, are described again in Chap. 5.
Typical detail engineering work includes:
 Purchasing activities, such as ordering:
- Machinery, apparatus and other equipment
- Bulk material for piping, instrumentation and electrical engineering
- Chemicals, catalysts
4 1 Basis of the plant design
 Process engineering:
- Verification of process engineering data
- Create the PID
 Piping design with e.g.:
- Isometrics
- Piping diagrams
- Pipeline stress calculations ("stress calculations")
- Pipe class determination
 Construction Planning:
- Steel construction
- Solid construction
 Instrumentation
- SAS6
- Field devices
 Electrotechnical planning
 Scheduling (Level 3 and 4)
 Assembly engineering
1.3 Plant philosophy
Each plant follows an individual philosophy depending on the location and type of plant.
1.3.1 Plant locations
Plant location is a strategic decision and requires thorough planning. The location is the first far-reaching decision in a project. When the
decision about the location has been made, then it is difficult to change it. With the
Traditional site selection is based on economic and geographical factors.
off like
 Availability of raw materials,
 Availability of cheap energy,
 Availability of qualified workforce,
 good transport links for input materials and end products.
6 SAS D Safety and Automation System, see section 11.4.
1.3 Plant philosophy 5
Consequently, the selection of sites is influenced by political decisions
like
 Supply of cheap raw materials or raw materials;
 financial incentives, for example in the form of low taxes;
 Government subsidies of a direct or indirect nature, such as providing
from infrastructures.
Selection is therefore a very complex and wide-ranging issue. Today's
Markets are highly interconnected, well-trained personnel are not readily available, process technology can quickly become obsolete due to new technologies, and the
Site selection depends on environmental constraints and potential political upheaval.
As a consequence, companies decide on a large number of options and
these are based on the evaluation of all identifiable and possible options. This evaluation is the key factor for the site selection, and it consists of
 Operating Size Savings,
 Government Influences,
 Company interest.
Plant locations can be divided into two main categories: onshore and
the offshore locations. The term onshore or offshore is a term taken from the
oil and gas industry and is now also used for other industries (e.g.
Wind farms).
 Offshore plants are facilities that are installed offshore in the sea. These facilities can be upstream, midstream, or downstream. The focus is on facilities for the extraction and transmission of
energies, oils and gases.
 Onshore plants are plants that are built on land or near the coast.
In addition to the classification of onshore and offshore, it is important to know whether it is a
new plant or to upgrade (increase capacity) and modernize (reduce emissions, upgrade products, etc.) or expand a
existing plant. According to this, the sites can be classified as greenfield or brownfield.
1.3.2 Greenfield plants
A "greenfield" facility is one that is built on an undeveloped and previously unused industrial site. For a greenfield plant
6 1 Basis of the plant design
the complete infrastructure usually has to be installed. Greenfield plants are mostly
New facilities or facilities that are being relocated.
The typical problems with Greenfield are the connections of the plants to the existing infrastructure and the new infrastructure to be built.
1.3.3 Brownfield plants
A brownfield plant is a plant that is built on a developed site (e.g. brownfield site, industrial park) into an existing plant or subplant or into an industrial complex (e.g. BASF Ludwigshafen, Bayer Leverkusen). Typically
are plant expansions to increase production capacities ("revamp"), conversions due to process engineering necessities (e.g. environmental regulations) and new plants on industrial sites or brownfields that were previously used for other purposes. In the case of brownfield facilities, part of the infrastructure is usually already in place or is merely being added.
"Brownfields are real property, the expansion, redevelopment, or reuse of which may be
be complicated by the presence or potential presence of a hazardous substance, pollutant,
or contaminant. Cleaning up and reinvesting in these properties protects the environment,
reduces blight, and takes development pressures off green spaces and working lands."
(United States Environmental Protection Agency 2017)
When planning a facility on a brownfield site, one should consider as much as
possible to learn about this site in order to get a good overview of site problems
and to take them into account in the planning.
The typical problems with brownfield plants are:
Contamination Contamination is the presence of contamination due to
Pollutants in soils or buildings. Decontamination must sometimes be carried out under high
effort can be carried out. The decontaminated material (soil house excavation, concrete residues
etc.) is then stored in special landfills.
Explosive ordnance In Western Europe in particular, the presence of
The search for weapons ("warefare materials") from World Wars I and II is a problem. The search for warfare materials should be carried out at a very early stage of the project, so that in the
project schedule, disruptions (time delays) can be minimized. That the circumstance of explosive ordnance is a real and also serious problem is shown by the press release in Fig. 1.1.
Existing building stock When planning a facility on a brownfield site.
it happens very often that the existing documentation of the existing equipment
or parts of the plant and the infrastructure is incomplete, incorrect or not available at all.
Therefore, parallel to the planning, the actual status ("as-built") must be recorded on site.
Recording the current state of above-ground structures can be done by 3D laser scanning-.
1.3 Plant philosophy 7
Fig. 1.1 Report of detonation at BASF construction site.
(RP Online 2017)
ning or a manual measurement with transfer to the existing documentation.
and, in the case of subsurface structures, by radar measurements and by excavation or dredging.
Assembly of plant components Assembly of equipment, piping or other plant elements should not take place while the plant is in operation;
Smaller conversion measures can be carried out, but require a high degree of
of safety-related coordination effort.
Installation activities for a new plant with an ongoing plant operation at the edge of the construction field (pipe bridges or ancillary plants) also require a very high level of
of safety-related measures. Larger lifting operations should therefore only be carried out during
of a shutdown can take place.
Tie-ins of plant components The tie-ins of the new plants and the new
Plant components to the existing plants can only be connected during a shutdown or
shutdown" or "turnaround" of the existing plants or plant sections. Individual pipelines can be connected during operation.
("hot-taps"), in order to avoid a shutdown and start-up of the plants and an associated
to avoid loss of production.
The better the ratio between operator personnel (operating and maintenance personnel)
and the personnel of the planning and installation company, the easier the process will be.
Overall planning and installation process.
8 1 Basis of the plant design
1.4 Asset categorization
Facilities can be classified into three different categories. The oil and gas industry is a leader in this classification, and the following common classifications are used
made
Upstream facilities Upstream facilities are used to explore for, develop, and produce oil and gas wells, coal, ores or salts, or other naturally occurring resources. Typical upstream facilities are oil production platforms.
Midstream plants Midstream plants are used to connect the upstream and
Downstream facilities. Typical of these are subsea pipelines or transfer and
loading stations, but also gas liquefaction or gas purification plants.
Downstream plants Downstream plants are used to process raw materials,
these include, for example, refineries, petrochemical plants and fertilizer complexes.
2 Process engineering basis of the plant design
Process plant design is an important part of industrial plant design and is indicative of the overall project design.
The process engineering department first develops an overall plant concept that includes all the
Plant Units required for the realization of the project. The total plant is usually divided into
 process plants ("Process Plant and Process Unit") and
 Ancillary Facilities ("Offsites and Utilities").
A project can consist of only one or of several process plants (plant complex
or Plant Complex).
Based on the desired product quantities and quality requirements for the
products as well as from the legally and/or project-specifically permitted gaseous
and liquid emissions at the plant boundary (Battery Limit, BL) are initially
The process steps (unit operations) are designed for each process plant in order to achieve the
and qualities of raw materials and supplies required for production (e.g.
water, steam, electricity).
Based on this, the scope, process steps and interconnection of the required
Ancillary facilities determined, also based on what feedstock can be made available to the project at the facility boundary.
Since the ancillary systems themselves require certain raw materials and supplies, it is
the planning process is iterative and requires some experience (lessons learned) with the
type of plant to be planned. It is subject to an optimization process, which, however, is promptly
must be completed in order to establish a secure planning basis for further engineering processing.
Since the plant concept determines the plant scope as well as the plant complexity of the project, it essentially determines the investment in the project as well as the operating costs (raw material consumption) via the consumption figures. The plant concept is
© Springer-Verlag GmbH Germany, part of Springer Nature 2018 9
K. G. Topole, Fundamentals of Plant Design, https://doi.org/10.1007/978-3-662-57418-8_2
10 2 Process engineering basis of plant design
the major factor influencing the overall economics of the project. The
process engineering, it must therefore be known in which direction the project will be optimized.
should be and what the influencing factors are.
The determined plant configuration as well as the underlying Plant Units and their capacities are summarized in a design basis1 , which is one of the documents
for further engineering processing and is largely created by process engineering.
The design basis contains a great deal of information that is added to by all engineering disciplines during project execution. Only when the basic concept and
the basic information has been established, the other engineering trades can continue with the further
Start interpretation.
The process engineering design is thus the start for the engineering execution and provides the basic information for both the engineering execution and the specification and procurement of the necessary equipment.
Disposition.
For this purpose, the process engineering department, if necessary in cooperation with a licensor, provides, among other things, flow diagrams and all basic process engineering data (e.g. media,
material data) are available for the other engineering trades.
In addition, process engineering provides basic information for construction, assembly and the
later commissioning available. Process engineering takes the plant after
end of assembly in operation and demonstrates the guaranteed product qualities in the test run,
consumption and emissions. It is responsible for and thus influences the start-up and
the successful completion of a project execution.
2.1 Process engineering in the project organization
There are usually several phases in the execution of a project, some of which overlap and some of which build on each other. These phases are:
 Conceptual Engineering
 Basic engineering
 Detail engineering
 Procurement
 Construction and assembly ("construction")
 Commissioning
 Warranty runs and handover to the customer
A typical project flow can be represented chronologically as in Fig. 2.1.
Process engineering is responsible for two positions. On the one hand for process engineering, on the other hand for commissioning.
1 Design basis D Specifications, see section 4.1.
2.2 Responsibility and fundamentals of process engineering 11
Conceptual
Engineering
Basic
Engineering
Detail
Engineering
Procurement
(Procurement)
Construction and assembly
(Construction)
Commissioning
(Commissioning)
Handover
(Hand-over)
Fig. 2.1 Basic chronological sequence of the phases of a project execution in plant construction
The number of process engineers working on a project can vary greatly depending on the size of the project. In the simplest case, the
process engineering can be handled by only one employee (simple processes or
individual unit operations to be processed).
For complex plants, up to 60 process engineers or more can also be involved in
work on a project, such as at refineries or at large petrochemical complexes such as steam crackers with connected polymerization plants.
Usually, for process plants, it is assumed that at least one process engineer is available for each process plant. For ancillary plants ("offsites and
utilities") is often grouped by subject (e.g., water, steam, air, tank, storage).
In the case of more complex projects, the process provider or process engineering in the
Organization Chart represented by a Lead Engineer Process. The Lead Engineer Process
in turn leads its process team, which in turn may include lead engineers for the respective technologies or groups.
2.2 Responsibility and fundamentals of process engineering
in engineering planning
Within the scope of project execution, the process engineering planning department prepares, in addition to the
Development of the plant concept, among other things, the basic information for the other engineering disciplines.
These disciplines involved are essentially:
 Equipment engineering, e.g. for heat exchangers, vessels, reactors, separators,
Tank, pumps, compressors, steam turbines, gas turbines, etc.
 Location and layout planning, e.g. main dimensions of equipment, requirements for their horizontal and vertical orientation relative to each other, minimum or
maximum distances of the equipment from each other
 Pipeline engineering, e.g., pipeline diameters, fluid properties, pressures,
Temperatures
12 2 Process engineering basis of plant design
 Instrumentation, e.g. type, functional requirements, fluid properties, minimum,
normal, maximum or design conditions
 Electrical engineering
 Construction and steelwork
The information and documents produced by process engineering include
i. d. R.
 Process flow diagram (PFD)
 Pressures, temperatures and material composition of all material flows at every point in the plant
 associated substance values
 Process-relevant dimensions of equipment as well as specifications for machines and heat exchangers
 Piping and instrumentation diagram (PID)
 Locking description
 special requirements regarding safety and material requirements
 Quantity requirements of raw materials, consumables and supplies at the plant boundary
 Emissions at the plant boundary
The process engineering design and planning thus forms the basis for the
mechanical design and planning of the apparatus and piping as well as for the
Position and installation planning. The process engineering thus determines the timing,
when such information can be provided, the starting point of the
work of the other engineering disciplines and procurement.
At the start of the project, however, not all information is available to the process engineering department.
available. For this reason, process engineering must first work with reasonable initial assumptions and models, which are then modified accordingly in the course of subsequent processing.
validated and adapted.
Such later adjustments and, above all, possible errors are basically multiplied later in terms of required corrections in the other engineering trades.
This is generally acceptable to a certain extent in overall project management, especially if only documents need to be adapted, but it can lead to considerable problems.
if this results in changes to equipment that is already in the order or production or in the plant setup (changes to steel and
Concrete).
Close cooperation between the other engineering disciplines and process engineering, as well as agreed procedures for the handover and approval of documents, are therefore essential for successful project execution. Thus must
z. e. g. essential documents are released by both parties, for example
Inquiry and order specifications.
2.3 General tasks of process engineering in order processing 13
2.3 General tasks of process engineering
in order processing
In addition to the actual engineering work, the process engineering work has
processors in the project also have numerous general tasks to perform.
This includes, but is not limited to, the following project preparation and project support tasks:
 Evaluate the contract in terms of process-related and schedule-critical risks
as well as to relevant risks in relation to the fulfillment of process guarantees
 Establish hourly budgets for the planning of the process engineering sequence.
Processing as well as ensuring that sufficient procedural personnel are available
 Compiling and revising the work and technical instructions valid for the project
 Compilation of working documents, such as templates and sample documents
as well as lessons learned from previous relevant project implementations
 Coordination and definition of the interfaces to the other engineering disciplines as well as the documents to be handed over (in terms of time, content and responsibility).
her: who creates, who checks and who releases?)
 Clarification of the electronic tools with which the processing is carried out, as well as form
and format of the transferred data
 Procurement and study of rules and regulations, in particular also local rules and regulations with regard to their relevance
 Procurement of the required substance data and the safety data sheets
 Determine the main substance database and the substance data models to be used.
and their sources (e.g. substance database)
 Obtain safety-related key figures (e.g. from GESTIS2 or Gefahrstoffinfo) and describe safe handling.
 Adjustment of the units to the contractual requirements and communication of the
unit system with the other engineering disciplines
 Definition of a so-called PID0, in which the PID representation of all plant components to be represented is comprehensively and conclusively defined.
 Determine how equipment, piping, instrumentation, etc. is represented and numbered in the PID and coordinate with equipment design, electrical engineering, instrumentation, piping design, and installation design departments.
2 GESTIS D Substance database, hazardous substance information system of the German Social Accident Insurance.
14 2 Process engineering basis of plant design
 Assistance in defining interfaces between customers, consortia, partners, divisions, licensors or suppliers with regard to
- Engineering
- Delivery
- Documentation
- Decrease
- Commissioning
During project execution, Process Engineering shall perform the following tasks as part of the general execution organization:
 Continuous tracking of planning progress and hourly budgets
 Participation in project meetings
 Participate in reviews of documents with the customer as well as with suppliers (e.g.
PID Review and Model Review)
 Representation and communication of technology-relevant requirements in the project team
 Support of the assembly organization with regard to process-technical peculiarities and requirements
 Planning and coordination and, if necessary, organization of commissioning.
2.4 Process engineering interfaces with licensors
In most cases, the construction of process engineering plants is based on a procedure and
is based on a procedure provider. A distinction is made between processes that are realized without a license
technologies, so-called open-art technologies, and processes that can only be used under license.
of a licensor or technology provider can be planned and implemented. Open-art technologies are often found, for example, in the area of ancillary systems.
The exact data and parameters of a process engineering process are determined by the
so-called procedure giver responsibly determined.
The procedure provider can be
 the client or subsequent operator of the plant,
 of the plant engineers,
 a third party licensing the process to a plant builder or the plant operator.
2.5 Coordination with licensors 15
At the start of the planning and design of a plant, all outstanding procedural issues must be coordinated with the procedure provider. These include, for example:
 Confirmation of the offered process concept
 Reconciliation of necessary procedural changes due to change in design basis or tightening of contract guarantees.
 Coordination of the procedural steps, which are to be carried out by investigations at the procedure provider
(reference plants) still have to be carried out
Licensors can either be operators of chemical plants themselves (e.g.
Bayer, BASF, Shell, ExxonMobil, Dow Chemicals, Evonik), which have developed their technologies in the
The company only makes its own data available to third parties for its own projects, and generally only on a restrictive basis.
In addition, there are pure technology companies that conduct their business through the sale of
generate licenses (e.g. UOP, Topsoe, Axens). Finally, the third group consists of engineering companies with their own technology base and licensing processes, which generate a
can offer integrated engineering project management and project implementation (e.g. Linde, Lurgi, KBR, ThyssenKrupp Industrial Solutions, Technip).
In the first two cases, the licensor usually provides a licensor package, called a License Package or Process Design Package (PDP), for the process engineering. This is then developed by an engineering company
further elaborated in procedural or engineering terms. Such engineering companies
often do not have their own technologies to rule out know-how conflicts (e.g.
Bechtel, Fluor, Worley Parsons, Samsung, LG).
This creates an interface in the procedural handling between
Licensors and plant planners, who are observed and accompanied in terms of processing technology
must. This interface is relevant in both directions. On the one hand, the plant planner needs the most accurate possible knowledge of all process-related background information for further processing. On the other hand, the licensor needs the information feedback
from subsequent project execution (lessons learned).
Possible influences on the process engineering work, if the licensor and the equipment manufacturer are different, are described in the following section.
2.5 Coordination with licensors
As a rule, the plant designer is responsible for the hydraulic throughput of the plant (capacity), while the exact data and parameters of a process engineering process as well as the product qualities are determined by the so-called process giver (licensor).
be determined responsibly.
If the subsequent operator of the plant is himself or a third party who has delegated the process to a
plant constructor or the plant operator is involved, the plant planner must
16 2 Process engineering basis of plant design
Identify all process-related issues that arise in the course of processing and
clarify with the licensor.
The extent of such coordination and clarification usually decreases as the project progresses. A typical milestone is HAZOP3, in which the
safety and operational concept is laid down.
The communication and coordination with the licensor is then generally only
again increase with the start of commissioning activities and their planning.
Especially at the beginning of the planning and design of a plant, the coordination with the licensor is intensive. This essentially concerns the preparation of the
plant concept. In the process, all outstanding procedural issues must be coordinated with the procedure provider.
These include, for example:
 Optimization and confirmation of the offered process concept in terms of
Consumption figures, product qualities and investment costs (also CAPEX4 or
OPEX5 optimization)
 Development and coordination of the plant safety concept
 Coordination of necessary process changes due to changes in the design basis (e.g. emissions, winterization requirements, qualities of raw, auxiliary and
operating materials) or tightening of contract guarantees.
 Coordination of the procedural steps, which are to be carried out by investigations at the procedure provider
(referencing) still have to be carried out
 Reconciliation of material requirements
 Changes in consumption figures for raw materials and supplies
 Clarification of cost influences
 Influence on installation, space requirement of the plant and mass scaffolding
In the course of processing, adjustments are then made on an ongoing basis, which may involve
must be coordinated with the licensor. Decisive documents or information that must be agreed with the licensor, as a rule at least until the documents are frozen, are
must be coordinated are, for example
 Mass and energy balance
 Temporary and continuous consumption of raw materials, consumables and supplies both
during start-up and shutdown as well as in continuous plant operation
 emissions both during startup and shutdown and in continuous plant operation
 Substance data or their interpolation, extrapolation, limits and accuracies
3 HAZOP D Hazard and Operability Study, examination of the operational safety and operability of a plant, see section 13.2. 4 CAPEX D Capital Expense. 5 OPEX D Operating Expense.
2.5 Coordination with licensors 17
 Equipment list and, if applicable, apparatus and instrument types
 Process flow diagram
 Construction materials
 Piping and instrumentation diagram
 Locking description
 HAZOP
 Operating manual
As a general rule, a review and
Release procedure for documents and drawings can be agreed (e.g. for PID).
Joint consolidations or participation of the licensor in meetings with the subsequent plant operator can also be helpful (e.g., participation in the
HAZOP).
The chronological sequence of the intensity of the dialog between the plant designer and the procedure provider is shown schematically in Fig. 2.2.
As expected, the focus of the dialog lies in the concept phase and at the beginning of basic engineering. After that, during the detail engineering and during the
There is relatively little exchange during the construction and assembly phases of the plant. Towards the end of the assembly work, namely in the commissioning phase, the dialog with
the procedure provider again increases rapidly. Normally, even employees of the
The process engineer was sent to the construction site to supervise the commissioning on site.
Concept phase and BE EN Construction and assembly Commissioning
Time
Fig. 2.2 Dialog with the process generator along the time axis. BE Basic Engineering; DE Detail
Engineering
18 2 Process engineering basis of plant design
2.6 Development process of a technical plant
The development process of a technical plant can be divided into the following typical steps
be structured:
 Process development in laboratory and/or test facilities and/or determination
of material and design data including the corresponding plant setups
 Extrapolation to industrial scale (scale-up) in case of not yet realized in this process route or not yet referenced in this capacity.
Procedure
 Determination of the administrative, economic and technical framework conditions as well as the requirements of the plant operator with respect to the
Technology or the process to be implemented
 Feasibility study with technical and economic comparison of different concepts (CAPEX or OPEX optimization). This study usually ends in
a go-or-no-go decision as to whether a plant of this type will be built at all
 Concept phase/preliminary design, i.e. selection of the final concept and initial estimates of the technical scope of the plant, if necessary also initial cost and
Schedule estimates for the investment project against the background of the technical
Feasibility
 Elaboration of the technically and economically most advantageous concept and determination of all expected costs and revenues (design planning or basic engineering)
 Approval planning for obtaining the necessary approvals from the relevant authorities (authority engineering)
 Detailed design and exact description of all necessary components and
Measures for the realization (implementation planning or detail engineering)
 Request for the described (specified) components and services
 Offer comparison and order
 Track manufacturing for compliance with required standards and performance
with regard to quality and deadlines
 Construction and assembly of the plant
 Training of the customer personnel
 Commissioning and execution of warranty runs
Such work can be done either before the project execution and realization of a
plant construction project or they are part of the inquiry and project execution process.
2.7 Project phases of process engineering 19
2.7 Project phases of process engineering processing
Process engineering work is normally divided into two or three project phases during engineering processing, depending on whether basic engineering is subdivided again.
The depth and scope of processing in the respective phases are not standardized or firmly defined and must therefore be adapted to the project, customer and/or region.
be defined on a project-specific basis. For this purpose, a bill of quantities must be created for each project.
and a performance description (Scope of Work) must be prepared.
Additionally, the process engineering work is divided horizontally (the partners work on different plant units in one phase) and/or vertically (the work is
of partners build on each other) on different partners, an additional
Interface description (who does what? until when? in which depth and with which
Responsibility?) required (Split of Work).
Usually, the process engineering works are divided into
 Conceptual Engineering,
 Basic Engineering,
 Detail Engineering.
How an investor ultimately proceeds in handling a project is highly customer-dependent and also often varies from region to region. The scope of planning described here
However, it must generally be handled comprehensively, irrespective of the planning route.
2.7.1 Conceptual Engineering
Conceptual engineering is carried out either before the actual realization by the
Investor, if necessary with the support of consultants or engineering partners, itself
or the conceptual engineering is part of an overall invitation to tender to a
General Planner.
In practice, the investor has found that conceptual engineering
often carries out himself, if he is also the owner of the process and the plant
builds for itself.
A further consideration of conceptual engineering is given in chap. 3.
2.7.2 Basic engineering
The preparation of the basic engineering means that for the planned plant an initial in
self-contained documentation is created.
20 2 Process engineering basis of plant design
The basic engineering is based either on a conceptual engineering, an own process development or an own process or a licensed process. The scope of the basic engineering is agreed with the client and is
often represents the basis of the permit application.
Basic engineering can be implemented as a self-contained process or in the form of phases.
or an overall engineering design (basic and detail engineering).
A further consideration of basic engineering is given in chap. 4, and a
Further consideration of detail engineering is given in chapter 5.
2.7.3 Division of basic engineering into phases
Basic engineering can be further divided into two phases. Since these
subdivision often takes place in international projects, here the international
Terms used:
 Process Design Package (PDP) and
 Front-End Engineering Design (FEED).
Often, such subdivisions follow the requirements of phased approaches to project delivery that follow either internal project approval approaches (shareholder identification, determination, and approvals of investment budgets) or requirements of financial institutions.
In fact, however, a phased approach may be enforced by an interface between the licensor and the plant designer. For example, the operator creates a phase based on
a PDP using its own technology, which is then taken over by a plant designer for processing and further elaboration.
2.8 International terms and abbreviations
in process engineering
A number of internationally used abbreviations are generally used in process engineering. The most important ones are summarized here:
BE Basic Engineering
BEP Basic Engineering Package
BFD Block Flow Diagram
DE Detail Engineering
FEED Front-End Engineering Design
FEL Front-End Loading
GES General Engineering Specification
2.9 Process simulation 21
HAZOP Hazard and Operability Study
MTO Material Take-Off
PDP Process Design Package
PEP Process Engineering Package
PFD Process Flow Diagram
PID Pipe and Instrument Diagram
For the description of the planning states of engineering documents have become established in
status abbreviations have been established in many industries. They are country-, company- and customer-specific, sometimes even project-specific, and may well differ. Recurring
internationally used status abbreviations are:
IFR Issued for Review
IFD Issued for Design (e.g. for HAZOP)
IFDD Issued for Detail Design (includes HAZOP results).
IFC Issued for Construction
2.9 Process simulation
In the broadest sense, process simulation is the emulation of a process engineering process through computer-based modeling. The fields of application of the
Process simulation is multifaceted and includes the determination of mass and energy balances and investigation of reaction kinetics in the context of process development
as well as the detailed analysis of production operations, the support of complex control concepts or the training of operating personnel. As a result of the increasing
understanding of complex physical and chemical processes is a reality-based
mathematical modeling of a process is possible. Through today's possibility,
with current tools even very comprehensive mathematical models in real time.
emulate, the importance of process simulation in development, construction and
in the operation of chemical process plants is increasing significantly.6
For a reliable process simulation, sound knowledge of the system to be modeled is required. This essentially includes:
 The substance system: Which chemical substances are present? What are the main components in the system and what impurities/trace components are present?
 Pure substance and mixture thermodynamics: how can pure substance properties (boiling point, vapor pressure, density, etc.) and phase equilibria (gaseous, liquid, solid) be
6 In recognition of the valuable and always very inspiring dialogs with Dr.-Ing. Ralf Bonmann, Hattingen.
22 2 Process engineering basis of plant design
be described? Which non-idealities occur (azeotropes, mixing gaps,
eutectics, etc.)?
 Heat and mass transfer: Which heat transfers are present? Are there mass transfer limitations at the phase interfaces?
 Reaction engineering: Which main and side reactions occur? What are the reaction kinetics?
 Process steps: Which process steps are used? Through which model
can the process step be described with sufficient accuracy?
 The permissible operating range: In which range is the operation of the plant permissible and in which range should it be described by the model? In which
Area are the models used valid?
Not all of the above information always needs to be available for a simulation. For example, without the exact knowledge of the reaction system, a mass and
energy balance can be prepared if analyses of chemical conversions are available for the operating point under investigation. In such cases, however, one must very precisely determine the
Note boundary conditions under which the simulation was created. For an extrapolation, i.e., a different operating point, this model would not be valid and would not provide any
provide reliable results.
It is also common to use simulation models of only a part of the process plant.
create. This reduces the model creation effort and model complexity.
When using these partial simulations, however, it must also be noted that
one is within the definition range of the model. In the presence of a solidly validated simulation model, even the design of complex new equipment, e.g. of
distillation or adsorption columns7 , without accompanying laboratory or pilot plant tests.
The result of a successful process simulation is a closed-loop thermal and
Material balance for the overall process and for the provision of
 Material flows and their composition (material and phase fraction);
 operating pressures, operating temperatures, phase condition and enthalpies;
 heat quantities to be absorbed or dissipated (e.g. with heat exchangers or
Evaporator);
 Material and mixture data (e.g. dynamic or kinematic viscosities, heat capacities, densities).
In principle, two groups of simulations can be distinguished, static and
the dynamic simulation.
7 Adsorption, see section 9.2.2.
2.9 Process simulation 23
2.9.1 Static simulation
Static simulations describe a steady state, i.e. a state in the system without consideration of a change over time. This can be the design case of a
process or any other operating case, e.g. 80 % load, summer operation or winter operation. Static simulations are required during process development
an important tool for drawing up the mass and energy balance, for determining
hydraulic parameters or for load data in equipment design.
There are several commercially available static process simulators for chemical
and petrochemical process plants. These include Aspen Plus8 and Aspen HYSIS9,
both from the ASPEN Engineering Suite, PRO/II10, ChemCAD11 or SINET12, to just
to name a few. ASPEN Plus, ASPEN HYSIS and ChemCAD have a focus on
used for processes in the chemical industry, while PRO/II is frequently used in the
is used in the petrochemical industry. In addition, some large companies have their own
developments in use. An example of this is the simulation package Chemasim of the
BASF called.
Static simulators are divided into sequential and equation-oriented models. Sequential models calculate on the basis of fixed defined input variables
a result. Therefore, all input streams and model parameters of a process step must be known so that the calculation can be performed. Calculated are then the
Outlet currents and operating conditions of the process unit. These then define the
Entry condition for the next process step, as shown in Fig. 2.3.
Sequential approaches have the advantage of mostly robust convergence, since the models get by with comparatively few degrees of freedom. Through the calculation
one process step at a time, feedback streams require an iterative approach,
so that sequential simulators for complex interconnections with feedback currents have to calculate each process step several times until all feedbacks have converged.
This process can be improved by the appropriate choice of estimated values as the starting point for the
Fig. 2.3 Static model
with unknown parameters
on the output side
Model
Model parameters
: Model parameters
: Pressure
: Volume flow
: Composition
8 Aspen Plus: http://home.aspentech.com/products/engineering/aspen-plus. 9 Aspen HYSIS: http://home.aspentech.com/products/engineering/aspen-hysys. 10 PRO/II: http://software.schneider-electric.com/products/simsci/design/pro-ii. 11 ChemCAD: https://www.chemstations.eu/. 12 SINET: http://www.epcon.com/sinet.html.
24 2 Process engineering basis of plant design
Model
Model parameters?
Fig. 2.4 Static model with unknown parameters on the input and output side
and unknown model parameters themselves
feedback streams can be accelerated. However, long computation times can still occur, especially in processes with many nested feedbacks. The time required in the
chemical industry most widely used commercial process simulators with
sequential approach are ASPEN Plus and PRO/II, whereby ASPEN Plus also
offers an equation-oriented solution algorithm.
Equation-oriented simulators follow a different approach. Here the process
mapped into a system of complex equations, which are simultaneously solved with a mathematical equation solving algorithm. This approach offers the advantage,
that input variables of a model can also be calculated, if instead the
output variables are present, as shown in Fig. 2.4. This allows systems with
complex returns often calculate better.
A disadvantage of the equation-oriented approach is the higher complexity
of the required solution algorithms and the associated often more difficult convergence in finding solutions. Typical representatives for equation-oriented
Process simulators are ASPEN HYSIS or ChemCAD.
2.9.2 Dynamic simulation
Compared to static simulations, dynamic simulations additionally consider
the change in time between a fixed start time and an end time.
The starting point for a dynamic simulation is a converged static simulation.
In addition to the input variables for the static model, further parameters must be defined for the dynamic simulation. These include dead times in the system, such as those
supply long pipelines, the hold-up of the apparatus under consideration and the existing
regulations. As a result, dynamic simulations are more complex than static ones and clearly
more time-consuming to create. They are often only used specifically in areas where the time
process of a change is relevant to the process and the higher effort of the dynamic
Model creation justified.
Typical application areas for dynamic simulations are, for example, load change scenarios for which control concepts have to be created that meet certain boundary conditions.
fulfill. One such boundary condition may be, for example, that a temperature is not exceeded during the transition from one state to the other. This
Questions are often connected with the safety concept of the plant or the
2.9 Process simulation 25
Determination of hazards in plant operation. Likewise, dynamic simulation can be used to validate operational procedures or safety protection circuits.
be used if the risk assessment or operational constraints preclude an operational test.
A special case of the application of dynamic simulators are the so-called Operator Training Systems (OTS, training simulators). These systems allow the operating personnel to practice the operation of a plant before the plant is completed or to train hazardous situations without having to risk endangering the operation. OTS
emulate a process with connected process control system in real time. For this
a robust and, above all, fast dynamic simulation model is required. In the best case, the user interface of the OTS is identical to that of the later control system. At
new plants today, the OTS is very often created in parallel with the engineering.
Another special case for dynamic simulations with growing importance is
Model Predictive Control (MPC). This is an advanced automation of the multivariable controller (Advanced Process Control, APC). Multivariable controller
control a large number of different manipulated variables on the basis of a linearized model of the
Control parameters. MPC goes one step further: Here, the predictive specification of the
Control variables based on the calculations of a dynamic simulation model."""


# In[6]:


#@title Environment Vars
openai_api_key = "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"


# In[7]:


import os
os.environ["OPENAI_API_KEY"] = openai_api_key


# In[8]:


from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain import OpenAI, VectorDBQA


text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_text(text_model_input)

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(texts, embeddings)


# In[9]:


qa = VectorDBQA.from_chain_type(llm=OpenAI(), chain_type="stuff", vectorstore=vectorstore)


# In[10]:


query = "What is the basis of plant design"
qa.run(query)


# In[11]:


llm = OpenAI()
llm(query)


# In[12]:


from langchain.chains import load_chain

chain = load_chain("lc://chains/vector-db-qa/stuff/chain.json", vectorstore=vectorstore)


# In[13]:


query = "What is project planning?"
chain.run(query)


# In[14]:


# anvil.server.connect("server_LD74RT6KDAXRKT7NQHPIQDI6-PIQPHEM4TNNBOZY7")


# # In[15]:


# @anvil.server.callable
def user_query(user_input, server_response):
  return chain.run(user_input)


# In[ ]:


# anvil.server.wait_forever()

