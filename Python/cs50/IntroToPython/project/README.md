# X12 EDI Viewer
#### Video Demo:  <URL HERE>
#### Description:
The X12 EDI Viewer aims to provide a human friendly view of machine readable X12 EDI documents.

Electronic Data Interchange (EDI) is the computer-to-computer exchange of business documents in a standard electronic format between business partners. The term EDI encompasses the entire electronic data interchange process including the transmission, message flow, document format, and software used to interpret the documents. EDI standards describe the format of the electronic documents. One such standard is [X12](https://x12.org/) which was developed more than 40 years ago but remains relevant today in the worlds of Finance, Health Care, Insurance, Supply Chain, Transportation, Defense, and Aerospace. 

X12 supports a variety of [documents](https://en.wikipedia.org/wiki/X12_Document_List), also known as Transaction Sets. These Transaction Sets provide the blueprint that must be followed when creating documents for a specific purpose. For example, if you wanted to check the insurance eligibily of a patient you would construct, and send, a 270: Eligibility, Coverage, or Benefit Inquiry Transaction Set. In return you would expect to receive a 271: Eligibility, Coverage, or Benefit Information in response (if everything went well).

If there was an error in your syntax or invalid information was provided, then you would expect to receive a 999: Implementation Acknowledgement that included information as to why the request could not be responded to normally. As a developer, or user of a system that utilizes EDI, it is very common to receive a certain percentage of errors for which you only have machine readable data to decypher. To do so, you have to have an intimate understanding of the specifications for not only EDI in general but for the Transaction Sets involved. 

##### EDI Specification
EDI uses simple constructs to allow for complex business scenarios. At the core there are three types of data; Segment, Element, and Sub-Element. Delimiters are used to distinguish between them. The following represents a segment in EDI

```
ST*270*1234*005010X279A1~
```

Broken out, this represents the following data.

|Element|Description|
|-------|-----------|
|ST|The name of the segment|
|270|Transaction Set ID Code|
|1234|Transaction Set Control Number|
|005010X279A1|Implementation Convention Reference|

A full request for eligibility information would look something like the following:

```
ST*270*1234*005010X279A1~BHT*0022*13*10001234*20060501*1319~HL*1**20*1~NM1*PR*2*ABC COMPANY*****PI*842610001~HL*2*1*21*1~NM1*1P*2*BONE AND JOINT CLINIC*****SV*2000035~HL*3*2*22*0~TRN*1*93175-012547*9877281234~NM1*IL*1*SMITH*ROBERT****MI*11122333301~DMG*D8*19430519~DTP*291*D8*20060501~EQ*30~SE*13*1234~
```

An experienced EDI developer with knowledge of the 270 specification could probably identify most elements in this Transaction Set. For the unknown elements, you would have to refer to the documentation. The rules describing each element for this Transaction Set is defined in an implementation guide referenced in the ST segments first data element (ST01 = 005010X279A1). Some implementations have specifications that are hundreds of pages long so it can become very tedious to troubleshoot. Compounding the difficulty is the fact that most error responses only reference specify segments and data elements by code or position rather than canonical name.

There is additional [complexity](https://justransform.com/edi-essentials/edi-structure/) in structuring an EDI message (Interchange Control Structure) but that is outside the scope of defining the problem that this application aims to solve.