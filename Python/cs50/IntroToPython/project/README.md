# X12 EDI Viewer
#### Video Demo:  <URL HERE>
#### Description:
The X12 EDI Viewer aims to provide a human friendly view of machine readable X12 EDI documents. It uses [OpenEDI](https://github.com/EdiNation/OpenEDI-Specification) specifications as a guide to format EDI files.

Electronic Data Interchange (EDI) is the computer-to-computer exchange of business documents in a standard electronic format between business partners. The term EDI encompasses the entire electronic data interchange process including the transmission, message flow, document format, and software used to interpret the documents. EDI standards describe the format of the electronic documents. One such standard is [X12](https://x12.org/) which was developed more than 40 years ago but remains relevant today in the worlds of Finance, Health Care, Insurance, Supply Chain, Transportation, Defense, and Aerospace. 

X12 supports a variety of [documents](https://en.wikipedia.org/wiki/X12_Document_List), also known as Transaction Sets. These Transaction Sets provide the blueprint that must be followed when creating documents for a specific purpose. For example, if you wanted to check the insurance eligibily of a patient you would construct, and send, a 270: Eligibility, Coverage, or Benefit Inquiry Transaction Set. In return you would expect to receive a 271: Eligibility, Coverage, or Benefit Information in response (if everything went well).

##### EDI Specification
EDI uses simple constructs to allow for complex, hierarchical representations of data for specific business scenarios. At the core there are three types of data; Segment, Element, and Sub-Element. Delimiters are used to distinguish between them. The following represents a segment in EDI

```
ST*270*1234*005010X279A1~
```

Broken out, this represents the following data elements.

|Element|Description|
|-------|-----------|
|ST|The name of the segment|
|270|Transaction Set ID Code|
|1234|Transaction Set Control Number|
|005010X279A1|Implementation Convention Reference|

A full request for eligibility information would look something like the following:

```
ISA*00*          *00*          *ZZ*123456789012345*ZZ*123456789012346*080503*1705*>*00501*000010216*0*T*:~GS*HS*1234567890*1234567890*20080503*1705*20213*X*005010X279A1~ST*270*1235*005010X279A1~BHT*0022*13*10001235*20060501*1320~HL*1**20*1~NM1*PR*2*ABC COMPANY*****PI*842610001~HL*2*1*21*1~NM1*1P*1*JONES*MARCUS****SV*0202034~HL*3*2*22*1~NM1*IL*1******MI*11122333301~HL*4*3*23*0~TRN*1*93175-012547*9877281234~NM1*03*1*SMITH*MARY~DMG*D8*19781014~DTP*291*D8*20060501~EQ*30~SE*15*1235~GE*1*20213~IEA*1*000010216~
```


This flat structure represents the following hierarchy:

```
Interchange Control
    ISA Segment
    Functional Group 
        GS Segment
        Transaction Set 
            ST Segment
            BHT Segment
            Loop 2000
                HL Segment
                Loop 2100A
                    NM1 Segment
                Loop 2000B
                    HL Segment
                    Loop 2100B
                        NM1 Segment
                    Loop 2000C
                        HL Segment
                        Loop 2100C
                            NM1 Segment
                        Loop 2000D
                            HL Segment
                            TRN Segment
                            Loop 2100D
                                NM1 Segment
                                DMG Segment
                                DTP Segment
                                Loop 2110D
                                    EQ Segment
        End Transaction Set
            SE Segment
    End Functional Group
        SE Segment
End Interchange Control
    IEA Segment

```

This specific hierarchy is defined in the implementation guide for the X12 270 Transaction Set, specifically the 5010 version 005010X279A1. It is one such representation as Loops can be optional and/or repeatable. Segments and elements can also be optional and/or repeatable. The challenge lies in determining where in the hierarchy a specific segment belongs. Specifically, Loops are the most challenging as there is no 'Loop' or 'End Loop' segment.

##### Methodology
Given a EDI file, perform the following steps:

- Parse the EDI file into a list of Segments
- Discover all OpenEDI specifications contained in an openedi_schemas sub-directory and map the file path to a key comprised of the type and implementation
- Determine the type and implementation of the EDI file using the Functional Group (GS Segment) and first Transaction Set (ST Segment)
- Load the appropriate OpenEDI specification based on the EDI files type and implementation
- Iterate the list of segments while building a hierarchical object model using the OpenEDI specfication as a guide
- Display the hierarchical object model using [rich.Tree](https://rich.readthedocs.io/en/stable/tree.html)
