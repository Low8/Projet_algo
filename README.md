# Algorithms and Combinatorial Optimization Project

---

## Introduction

Since the 90s, there has been a truly global awareness of the need to reduce energy consumption and greenhouse gas emissions. The first commitments emerged when the Kyoto Protocol was signed in 1997. However, this protocol only entered into force in 2005, and many scientists believed that the efforts to slow down global warming were not enough. Since then, other more ambitious commitments have seen the light of day (France’s commitment to a 75 % reduction in emissions by 2050, for example, commitments made by certain large cities such as Paris). But the task is complicated. The government and local authorities are unable to force companies and individuals to change their habits in order to meet these goals. Therefore, action is primarily focused on changing behaviour. Saving and recycling raw materials, improving means of transport and the energy performance of buildings should become priorities.

## DESCRIPTION

ADEME (French Environment and Energy Management Agency) has recently launched a call for expressions of interest to promote the execution of demos and experiments of new mobility solutions for people and goods, adapted to different kinds of territories.

Your CesiCDP structure is already well established in the field. With the help of many partners, you have carried out several studies on Smart Multimodal Mobility. New transport technologies, despite being more cost-effective and cleaner, also pose new challenges, particularly in terms of resource management optimization. But these transport logistics problems present a major challenge for the future: they can be applied in many areas (mail distribution, product delivery, road network maintenance, garbage collection) and their impact on the environment can be truly significant.

You are part of the team set up by CesiCDP to answer the call from ADEME. The challenge is to win new markets with very attractive financing schemes to keep developing your business activity.

CesiCDP decided to focus its study on the management of delivery routes. The algorithmic problem consists in calculating on a road network a route allowing to connect a subset of cities between them, then to return to its starting point, so as to minimize the total duration of the route. This optimization should take into account the expected traffic on each axis for the different time slots.

The idea is to propose a method from Operations Research to generate a delivery route corresponding to this problem.

Even though the scope is yet to be defined, you have outlined a basic version of the problem. But you hesitate in adding additional constraints in order to make it more realistic and get ADEME’s full attention. One should expect the problem to be harder to address like this.

 

### Basic version

- Selecting the model and code in Python capable of solving large instances (several thousand cities)

- A statistical study regarding the algorithm’s experimental performance

 

### Additional constraints

Here is a (non-comprehensive) list of constraints that could be incorporated into your study scope. For some of them, advanced versions are also provided. Please note that implementing one constraint and any of its advanced versions is the same as implementing two constraints.

- Delivery time slot for each item

- No deliveries allowed beyond the time slot

- Waiting on site for the time slot to open is a possibility

- k trucks simultaneously available to make deliveries. The route calculation will have to include the allocation of items (and therefore the delivery points) to the different trucks available, and instead of minimising the total time, one should minimize the date when the last truck returns to base.

- Truck capacity (2 or 3 dimensions) and item footprint

- Some items can only be delivered by certain trucks

- Each item has a specific collection point

- The travel time of an edge varies over time (which is equivalent to varying its length), to represent the variation in traffic flow

These constraints can be divided into two categories:

- Constraints that do not change the space for solutions, only their values. For example, by taking into account time slots where waiting is required (if the truck is ahead of schedule). In the case of a neighbourhood-based method, the neighbours of a solution will not be changed by incorporating this constraint, only the costs will be different

- Constraints that change the space for solutions. For example, some items that require a specific type of truck for being delivered. Adding this constraint will render some solutions invalid, and consequently limit the space for solutions.


Other constraints can be addressed, if this is justified by an industrial application (not necessarily resulting from the current context).

## Required Python Libraries

To implement and test the Vehicle Routing Problem (VRP) algorithms, the following Python libraries are required.


| Library | Description |
|----------|--------------|
| **numpy** | Numerical computations and array manipulation |
| **pandas** | Data handling and analysis |
| **matplotlib** | Visualization of routes and performance metrics |
| **networkx** | Graph representation and manipulation |
| **vrplib** | Import of benchmark VRP and VRPTW instances (e.g., Solomon datasets) |
| **PuLP** | Linear programming solver used for optimization |
| **scipy** |  |

### Installation

Install the core dependencies:

```bash
pip install numpy pandas matplotlib networkx vrplib pulp

