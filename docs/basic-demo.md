# Basic Voice Demo

The basic voice service scenario is as follows:
1. Turn on base shared infrastructure
2. Create voice service with a single IPPBX server in the scaling pool
3. Run SIPP traffic simulator
4. Run another SIPP traffic simulator which should trigger a scaling event
5. Kill an IPPBX virtual machine which will trigger a healing event
