# Chapter 17: Blockchain and Distributed Ledger Technology in Regulatory Compliance

*"The immutable, transparent, and decentralised nature of blockchain creates unprecedented opportunities for building trust and accountability into regulatory systems, yet the technology's complexity and resource requirements demand careful evaluation against traditional alternatives."*

## Introduction

The intersection of blockchain and distributed ledger technology (DLT) with regulatory technology represents one of the most transformative yet controversial developments in the field of regulatory compliance. As we explore this topic, we find ourselves not merely discussing a new technology stack, but rather examining a fundamental shift in how trust, transparency, and accountability can be engineered into regulatory systems. The journey from blockchain's experimental origins to its current position as a practical tool for regulatory compliance has been marked by both remarkable successes and significant challenges.

The regulatory technology community has witnessed blockchain evolve from an experimental concept to a practical tool for regulatory compliance. The Bank of England's 2016 discussion paper on central bank digital currencies marked a turning point in regulatory acceptance, demonstrating that central authorities were beginning to seriously consider blockchain's potential for regulatory applications (Bank of England, 2016). This evolution reflects a broader recognition that distributed ledger technology offers unique capabilities for addressing long-standing challenges in regulatory compliance, from real-time transparency to automated enforcement of regulatory requirements.

However, the path to blockchain adoption in regulated environments has not been without obstacles. The technology's proponents often highlight its transformative potential, pointing to successful implementations like the Monetary Authority of Singapore's Project Ubin, which reduced interbank settlement times from days to minutes whilst maintaining full regulatory compliance and auditability. Yet critics argue that blockchain implementations face significant scalability, energy consumption, and regulatory uncertainty challenges that are often understated in discussions of the technology's benefits.

This chapter examines the complex landscape of blockchain and distributed ledger technology in regulatory compliance, drawing insights from a comprehensive workshop discussion that brought together diverse perspectives on the technology's potential and limitations. Through this exploration, we aim to provide a balanced assessment of blockchain's role in regulatory technology, examining both its transformative opportunities and practical challenges.

## The Regulatory Technology Landscape and Blockchain

Blockchain and distributed ledger technology represent a revolutionary opportunity for regulatory technology, offering the potential to fundamentally transform how organisations approach compliance, transparency, and regulatory reporting. The immutable, transparent, and decentralised nature of blockchain creates unprecedented opportunities for building trust and accountability into regulatory systems. However, the reality of implementation reveals significant gaps between theoretical benefits and practical outcomes that must be carefully considered.

### Current State of Blockchain in Regulatory Compliance

The current landscape shows blockchain being actively deployed across several regulatory domains, with varying degrees of success and adoption. Financial services represents the most mature application area, with initiatives like the Monetary Authority of Singapore's Project Ubin demonstrating successful implementation of blockchain for interbank payments and regulatory reporting. The European Central Bank's digital euro project represents another significant development in this space, showing how blockchain can be used to create programmable money that automatically enforces regulatory requirements.

Supply chain management has also seen substantial blockchain adoption, particularly in pharmaceuticals and food safety. The US Food and Drug Administration's pilot programme for drug supply chain security demonstrates regulatory support for blockchain-based tracking systems, while initiatives like TradeLens (IBM/Maersk) have processed over 30 million shipping events, demonstrating the scalability and reliability of blockchain technology in regulated supply chain management.

Digital identity solutions using blockchain are gaining traction, with Estonia's e-Residency programme and the European Union's digital identity framework incorporating distributed ledger concepts. The Estonian government's KSI blockchain implementation has processed over 1 billion digital signatures, demonstrating the reliability and security of blockchain technology in government applications with 99.99% uptime whilst maintaining full regulatory compliance.

### Technical Architecture Considerations

From a regulatory technology perspective, blockchain implementations must address several critical architectural concerns that go beyond traditional application development. The immutable nature of blockchain data, combined with regulatory requirements for auditability and transparency, demands exceptional attention to code quality, security, and testing practices.

**Consensus Mechanisms**: The choice between proof-of-work, proof-of-stake, and other consensus mechanisms has significant implications for regulatory compliance. Energy consumption, finality guarantees, and governance structures all impact regulatory acceptability. The Bitcoin network's 7 transactions per second limit demonstrates the fundamental trade-off between decentralisation and performance, while Ethereum's current throughput of approximately 15 transactions per second is woefully inadequate for large-scale regulatory applications.

**Privacy and Confidentiality**: Regulatory requirements often conflict with blockchain's inherent transparency. Solutions like zero-knowledge proofs and confidential transactions are becoming essential for compliant implementations. The immutable nature of blockchain conflicts with data protection regulations like GDPR, which include "right to be forgotten" provisions, creating potential compliance violations.

**Interoperability**: The fragmented nature of blockchain networks creates challenges for regulatory oversight. Cross-chain protocols and standardisation efforts are crucial for regulatory acceptance, as the distributed nature of blockchain technology challenges traditional regulatory authority structures, requiring new approaches to governance and oversight.

## Smart Contracts: The Promise and Reality of Automated Compliance

Smart contracts represent perhaps the most promising yet challenging aspect of blockchain in regulatory technology. The concept of self-executing contracts with embedded regulatory logic offers unprecedented automation possibilities, but also introduces new risks and complexities that traditional systems avoid.

### The Transformative Potential

Smart contracts offer the potential for real-time compliance monitoring and automated regulatory reporting. The European Central Bank's digital euro project demonstrates how smart contracts can be designed to automatically enforce regulatory requirements, reducing human error and ensuring consistent compliance across all transactions. In the pharmaceutical sector, smart contracts are being used to automatically track drug provenance and ensure compliance with regulatory requirements throughout the supply chain, not only reducing compliance costs but also enhancing patient safety by providing real-time verification of drug authenticity and regulatory compliance.

The benefits extend beyond financial services and supply chain management. Carbon credit trading platforms are emerging as effective tools for environmental regulatory compliance, providing transparent and auditable tracking of carbon emissions and credits. Clinical trial data management systems are using blockchain technology to ensure the integrity and regulatory compliance of clinical trial data, providing immutable audit trails for regulatory submissions.

### The Challenges of Implementation

However, smart contracts are frequently presented as a panacea for regulatory compliance, promising automated enforcement of rules and elimination of human error. This oversimplification ignores fundamental challenges that make smart contracts problematic in regulated environments.

**Legal Uncertainty**: The legal status of smart contracts remains unclear in most jurisdictions. The UK Law Commission's 2021 consultation on smart contracts highlighted numerous legal uncertainties, including questions about enforceability, liability, and dispute resolution. When smart contracts fail or produce unintended outcomes, there is often no clear legal framework for resolution. The DAO hack of 2016, which resulted in the theft of $60 million worth of Ether, demonstrates the legal complexities of smart contract failures, requiring a controversial "hard fork" of the Ethereum network to recover funds.

**Code as Law Problems**: The principle of "code is law" creates inflexibility that conflicts with the dynamic nature of regulatory requirements. Regulations change frequently, and smart contracts cannot be easily updated to reflect new requirements. This creates a fundamental tension between blockchain's immutability and the need for regulatory adaptability.

**Security Vulnerabilities**: Smart contracts are notoriously difficult to secure. The reentrancy vulnerability that enabled the DAO hack is just one example of how seemingly simple code can contain critical security flaws. Formal verification tools exist but are complex to use and cannot guarantee security for all possible scenarios.

### Software Engineering Requirements

Building blockchain applications for regulated environments presents unique software engineering challenges that go beyond traditional application development. The immutable nature of blockchain data, combined with regulatory requirements for auditability and transparency, demands exceptional attention to code quality, security, and testing practices.

Smart contract development for regulated environments requires a fundamentally different approach to software engineering. The Ethereum Foundation's Solidity documentation emphasises the importance of security-first development practices, but regulatory environments demand even higher standards. Tools like Certora and TLA+ provide formal verification capabilities for smart contracts, enabling mathematical proof of contract correctness, which becomes not just a best practice but a regulatory requirement in many jurisdictions.

Comprehensive testing must include unit tests for individual contract functions, integration tests for contract interactions, gas optimisation tests for cost efficiency, security tests for common vulnerabilities (reentrancy, overflow, etc.), and regulatory compliance tests for business logic validation. Third-party security audits are essential for regulated environments, with companies like ConsenSys Diligence and OpenZeppelin providing specialised blockchain security auditing services that meet regulatory standards.

## Distributed Governance and Regulatory Frameworks

Distributed governance models enabled by blockchain technology offer exciting opportunities for regulatory innovation, but they also challenge traditional regulatory authority structures, requiring new approaches to governance and oversight. The Estonian government's KSI blockchain implementation demonstrates how distributed ledger technology can enhance government transparency whilst maintaining security and regulatory compliance, providing a model that has been adopted by other governments seeking to improve their regulatory technology infrastructure.

### The Challenge of Regulatory Authority

The distributed nature of blockchain technology challenges traditional regulatory authority structures, requiring new approaches to governance and oversight. The challenge lies in designing regulatory frameworks that can effectively oversee decentralised systems whilst maintaining the benefits of distributed governance. This requires careful consideration of how regulatory authority can be exercised in systems where no single entity has complete control, whilst ensuring that regulatory requirements can be effectively enforced.

The Financial Conduct Authority's (FCA) approach to cryptoasset regulation demonstrates the complexity of adapting traditional regulatory frameworks to blockchain technology. The FCA's guidance on cryptoassets categorises different types of blockchain-based assets according to their regulatory characteristics, requiring different compliance obligations based on their classification. This approach highlights the need for regulatory frameworks that can accommodate the diverse nature of blockchain implementations whilst maintaining effective oversight.

### Cross-Border Regulatory Coordination

The potential for cross-border regulatory coordination through blockchain is particularly exciting. The Financial Action Task Force's guidance on virtual assets, combined with initiatives like the European Union's MiCA regulation, demonstrates how blockchain can facilitate international regulatory harmonisation whilst maintaining jurisdictional sovereignty. However, the fragmented regulatory landscape for blockchain technology remains a significant challenge, creating compliance risks for organisations considering blockchain implementations.

The United States has taken a fragmented approach, with different agencies applying different regulatory frameworks to blockchain applications. The SEC treats some tokens as securities, the CFTC regulates others as commodities, and the IRS treats them as property for tax purposes. This regulatory uncertainty creates significant compliance risks and opportunities for regulatory arbitrage, where organisations might choose jurisdictions with more favourable regulations.

## Implementation Challenges and Operational Considerations

Real-world blockchain implementations have consistently revealed significant challenges that go beyond the theoretical benefits often discussed. The technology's complexity and resource requirements may not justify benefits for many regulatory use cases, particularly when compared to traditional database systems with proper audit trails and security measures.

### Scalability and Performance Limitations

Despite years of development, blockchain networks still struggle with basic scalability requirements. The much-touted "Layer 2" solutions like Polygon and Optimism introduce additional complexity and centralisation risks that undermine the core value proposition of decentralisation. For regulatory applications requiring high throughput, such as real-time transaction monitoring or large-scale reporting systems, blockchain technology simply cannot compete with traditional database systems that can handle thousands of transactions per second.

### Energy Consumption and Environmental Impact

The environmental cost of blockchain technology represents a significant regulatory and reputational risk that is often dismissed by proponents. Bitcoin's annual energy consumption exceeds that of entire countries like Argentina, whilst Ethereum's energy usage rivals that of medium-sized European nations. For organisations operating under environmental regulations or ESG requirements, the energy consumption of blockchain systems creates compliance challenges that traditional systems avoid. The European Union's proposed MiCA regulation includes environmental impact assessments for crypto-assets, reflecting growing regulatory concern about blockchain's environmental footprint.

### Development and Integration Complexity

Blockchain development requires specialised skills that are in short supply and command premium salaries. The complexity of blockchain systems often leads to extended development timelines and increased costs compared to traditional solutions. Integrating blockchain systems with existing regulatory infrastructure is often more complex than anticipated, as legacy systems were not designed to work with blockchain technology, requiring significant custom development and integration work.

Operating blockchain systems requires specialised knowledge and tools that many organisations lack. The distributed nature of blockchain networks creates operational challenges that traditional IT teams are not equipped to handle, requiring comprehensive monitoring and observability frameworks that exceed traditional application monitoring.

## Monitoring, Operations, and Compliance in Blockchain Systems

Blockchain and distributed ledger technology present unique monitoring challenges that traditional application monitoring frameworks cannot adequately address. The distributed, immutable, and consensus-driven nature of blockchain systems requires specialised monitoring approaches that can track both technical performance and regulatory compliance in real-time.

### Multi-Layer Monitoring Architecture

Effective blockchain monitoring requires a multi-layered approach that addresses different aspects of system performance. Network layer monitoring tracks peer-to-peer network health, block propagation times, and network synchronisation status across all nodes. Consensus layer monitoring focuses on consensus mechanism performance, including block production times, validator performance, and consensus failures. Application layer monitoring tracks smart contract execution, transaction throughput, and application-specific metrics, while compliance layer monitoring ensures real-time regulatory compliance across all blockchain operations.

The Bank of England's research on central bank digital currencies highlights the importance of comprehensive monitoring frameworks for blockchain systems in regulated environments, including real-time monitoring of transaction flows, consensus performance, and regulatory compliance metrics.

### Change Management in Immutable Systems

Change management in blockchain systems presents unique challenges due to the immutable nature of blockchain data and the distributed consensus required for system updates. Traditional change management processes must be significantly adapted to address these challenges whilst maintaining regulatory compliance.

Smart contract upgrades in regulated environments require careful orchestration to maintain system integrity and regulatory compliance. This includes pre-deployment validation with comprehensive testing and formal verification of new contract versions, staged deployment with gradual rollout and monitoring at each stage, pre-planned rollback mechanisms for failed upgrades, and proactive notification of regulatory authorities for significant system changes.

### Incident Response and Resilience Planning

Incident response procedures need adaptation for blockchain-specific failures including consensus failures and smart contract vulnerabilities. Resilience planning must address blockchain's distributed nature and potential for network partitions. The immutable nature of blockchain creates significant problems in regulated environments, particularly regarding regulatory change management and error correction.

When errors occur in blockchain systems, they cannot be easily corrected due to immutability, creating significant operational and compliance risks as incorrect data becomes permanently embedded in the system. This immutability paradox presents fundamental challenges for regulatory compliance, as regulations change frequently and blockchain systems may become non-compliant, requiring complex migration or replacement procedures.

## Case Studies and Real-World Applications

The practical application of blockchain technology in regulatory compliance has produced both notable successes and significant failures, providing valuable lessons for organisations considering blockchain implementations.

### Successful Implementations

**Project Ubin (Singapore)**: The Monetary Authority of Singapore's blockchain-based interbank payment system successfully reduced settlement times from days to minutes whilst maintaining full regulatory compliance. The project demonstrated cost savings of over 30% compared to traditional systems whilst enhancing transparency and auditability, providing a model for other jurisdictions.

**JPMorgan's JPM Coin**: JPMorgan's blockchain-based payment system processes over $1 billion in daily transactions, demonstrating the scalability and reliability of blockchain technology in regulated financial services. The system has achieved 99.9% uptime whilst maintaining full regulatory compliance.

**Estonia's KSI Blockchain**: The Estonian government's blockchain implementation has processed over 1 billion digital signatures, demonstrating the reliability and security of blockchain technology in government applications. The system has achieved 99.99% uptime whilst maintaining full regulatory compliance.

**TradeLens (IBM/Maersk)**: This blockchain-based supply chain platform has processed over 30 million shipping events, demonstrating the scalability and reliability of blockchain technology in regulated supply chain management. The platform has reduced documentation time by 40% whilst enhancing regulatory compliance.

### Challenges and Failures

However, real-world blockchain implementations have consistently failed to deliver on their promises in many cases, with projects experiencing significant cost overruns and operational challenges. The development complexity of blockchain systems often leads to extended development timelines and increased costs compared to traditional solutions. Many blockchain projects fail because they underestimate the true cost of implementation and operation, including specialised skills requirements, integration challenges, and operational complexity.

## Regulatory Framework Evolution

The regulatory landscape for blockchain technology continues to evolve, with different jurisdictions adopting varying approaches to blockchain regulation. The European Union's Markets in Crypto-Assets (MiCA) regulation provides a comprehensive framework for blockchain-based financial instruments, establishing clear requirements for smart contract governance, security, and regulatory reporting. This regulation demonstrates how traditional regulatory frameworks can be adapted to address the unique characteristics of blockchain technology whilst maintaining effective oversight and consumer protection.

The UK's approach to regulating cryptoassets demonstrates how existing regulatory frameworks can be adapted to address blockchain technology whilst maintaining effective oversight and consumer protection. However, the fragmented regulatory landscape creates opportunities for regulatory arbitrage, where organisations might choose jurisdictions with more favourable regulations, though this approach carries significant risks as regulatory frameworks continue to evolve and harmonise.

### International Coordination Efforts

The Financial Action Task Force's guidance on virtual assets provides a comprehensive framework for addressing the regulatory risks associated with blockchain technology, including anti-money laundering and counter-terrorism financing requirements. The Basel Committee on Banking Supervision's approach to cryptoasset regulation demonstrates how traditional banking regulators are adapting their frameworks to address blockchain technology whilst maintaining financial stability.

The International Organization of Securities Commissions (IOSCO) provides guidance on cryptoasset regulation that offers a framework for securities regulators to address blockchain-based financial instruments whilst maintaining investor protection. These international coordination efforts are crucial for addressing the borderless nature of blockchain technology and ensuring consistent regulatory oversight across jurisdictions.

## Risk Management and Compliance Assurance

Blockchain implementations introduce new categories of regulatory risk that must be addressed through comprehensive risk management frameworks. The Bank for International Settlements' (BIS) research on central bank digital currencies highlights the importance of addressing operational, legal, and reputational risks associated with blockchain implementations in regulated environments.

### Risk Categories

From a regulatory architecture perspective, risk management frameworks must be designed to address several key risk categories:

**Operational Risk**: The technical complexity of blockchain systems and their potential for system failures or security breaches. The distributed nature of blockchain networks creates operational challenges that traditional IT teams are not equipped to handle.

**Legal Risk**: The uncertain legal status of blockchain-based assets and smart contracts in many jurisdictions. The UK Law Commission's 2021 consultation on smart contracts highlighted numerous legal uncertainties that create compliance risks for organisations.

**Compliance Risk**: The challenges of ensuring regulatory compliance in decentralised systems where no single entity has complete control. The fragmented regulatory landscape creates significant compliance risks for organisations operating across multiple markets.

**Reputational Risk**: The potential for blockchain implementations to damage institutional reputation if not properly managed. The environmental impact of blockchain technology, particularly energy-intensive consensus mechanisms, creates reputational risks for organisations operating under ESG requirements.

### Mitigation Strategies

Organisations considering blockchain implementations should conduct comprehensive regulatory risk assessments that evaluate the full range of risks associated with blockchain implementations. This includes establishing regulatory compliance monitoring systems that ensure ongoing compliance with regulatory requirements, developing regulatory change management processes that can adapt to evolving regulatory requirements, and engaging with regulatory authorities early to ensure implementations align with regulatory expectations.

## Future Directions and Emerging Trends

The future of blockchain in regulatory technology is likely to be characterised by continued evolution and refinement rather than revolutionary transformation. Emerging trends suggest that blockchain adoption will be selective, with organisations choosing blockchain solutions only where they provide clear advantages over traditional alternatives.

### Technological Evolution

The development of more energy-efficient consensus mechanisms and improved scalability solutions will be crucial for broader blockchain adoption in regulated environments. The emergence of privacy-preserving technologies like zero-knowledge proofs and confidential transactions will be essential for addressing regulatory requirements for data protection and privacy.

Interoperability standards and cross-chain protocols will become increasingly important for regulatory oversight across multiple blockchain networks. The development of formal verification tools and comprehensive testing frameworks will be essential for ensuring the security and reliability of blockchain systems in regulated environments.

### Regulatory Evolution

Regulatory frameworks will continue to evolve to address the unique characteristics of blockchain technology whilst maintaining effective oversight. The development of international coordination mechanisms will be crucial for addressing the borderless nature of blockchain technology and ensuring consistent regulatory oversight across jurisdictions.

The establishment of regulatory sandboxes specifically for blockchain applications will facilitate innovation whilst maintaining oversight. The development of standardised reporting requirements for blockchain-based systems will ensure regulatory transparency whilst accommodating the unique characteristics of distributed ledger technology.

## Recommendations for Implementation

Based on the comprehensive analysis of blockchain technology in regulatory compliance, several key recommendations emerge for different stakeholders.

### For Regulatory Bodies

1. **Develop Clear Guidance**: Regulatory authorities should provide specific guidance on blockchain implementations, including technical standards and compliance requirements. The Monetary Authority of Singapore's approach to blockchain regulation provides a useful model for other jurisdictions.

2. **Establish Sandbox Environments**: Regulatory sandboxes specifically for blockchain applications can facilitate innovation whilst maintaining oversight. The UK's Financial Conduct Authority sandbox has demonstrated significant success in this area.

3. **Promote Standardisation**: Support industry efforts to develop common standards for blockchain implementations in regulated sectors, reducing fragmentation and compliance complexity.

4. **Address Legal Uncertainties**: Work to resolve legal uncertainties around smart contracts and blockchain-based assets, providing clear frameworks for enforcement and dispute resolution.

### For Technology Implementers

1. **Adopt Privacy-by-Design**: Implement privacy-preserving technologies from the outset rather than as afterthoughts. Zero-knowledge proofs and confidential transactions are becoming essential for compliant implementations.

2. **Ensure Auditability**: Design systems with comprehensive audit trails that meet regulatory requirements for transparency and accountability.

3. **Plan for Evolution**: Build flexibility into smart contract architectures to accommodate regulatory changes, including migration strategies and compliance monitoring procedures.

4. **Implement Comprehensive Testing**: Use formal verification tools and comprehensive testing frameworks to ensure the security and reliability of blockchain systems.

### For Organisations

1. **Conduct Thorough Risk Assessments**: Evaluate both technical and regulatory risks before implementing blockchain solutions, including comprehensive cost-benefit analyses that include all implementation, operational, and compliance costs.

2. **Evaluate Alternative Solutions**: In many cases, traditional database systems with proper audit trails and security measures can provide similar benefits to blockchain at lower cost and complexity.

3. **Start with Pilot Projects**: Begin with small-scale blockchain implementations to demonstrate value and build organisational confidence, understanding the technology's limitations and requirements before committing to large-scale implementations.

4. **Invest in Education**: Ensure teams understand both the technical and regulatory implications of blockchain implementations, including specialised skills development and training programmes.

## Conclusion

The intersection of blockchain and distributed ledger technology with regulatory compliance represents a complex and evolving landscape that offers both significant opportunities and substantial challenges. The technology's proponents highlight its transformative potential for regulatory transparency, automation, and trust, pointing to successful implementations that have achieved measurable benefits in cost savings, operational efficiency, and compliance enhancement.

However, the reality of blockchain implementation reveals significant gaps between theoretical benefits and practical outcomes. The technology faces fundamental limitations in scalability, energy consumption, and regulatory uncertainty that make it unsuitable for many regulatory applications. The complexity and resource requirements of blockchain systems may not justify their benefits when compared to traditional alternatives in many use cases.

The key to successful blockchain adoption in regulatory compliance lies in careful evaluation of the technology's suitability for specific use cases, comprehensive risk assessment, and thorough planning for implementation and operation. Organisations must weigh the potential benefits of blockchain technology against its significant costs and complexities, ensuring that blockchain solutions are chosen only where they provide clear advantages over traditional alternatives.

The future of blockchain in regulatory technology will likely be characterised by selective adoption rather than wholesale transformation. As the technology continues to evolve and regulatory frameworks mature, blockchain may find its place in specific regulatory applications where its unique characteristics provide clear value. However, the technology's limitations and challenges must be carefully considered in any implementation decision.

For regulatory technology professionals, the lesson is clear: blockchain technology is a powerful tool that can provide significant benefits in appropriate use cases, but it is not a panacea for regulatory compliance challenges. Success requires careful evaluation, thorough planning, and realistic expectations about the technology's capabilities and limitations. The key is to approach blockchain implementation with both enthusiasm for its potential and pragmatism about its challenges, ensuring that the technology serves the broader goals of effective regulatory compliance rather than becoming an end in itself.

As we continue to explore the evolving landscape of regulatory technology, blockchain and distributed ledger technology will undoubtedly play an important role in shaping the future of regulatory compliance. However, their success will depend on our ability to address the fundamental challenges they present whilst leveraging their unique capabilities to enhance regulatory effectiveness and efficiency.

## References

Bank of England. (2016). *Central Bank Digital Currency: Opportunities, Challenges and Design*. Discussion Paper. London: Bank of England.

Basel Committee on Banking Supervision. (2021). *Prudential Treatment of Cryptoasset Exposures*. Basel: Bank for International Settlements.

European Central Bank. (2020). *Report on a Digital Euro*. Frankfurt: European Central Bank.

European Union. (2023). *Markets in Crypto-Assets (MiCA) Regulation*. Official Journal of the European Union.

Financial Action Task Force. (2019). *Guidance for a Risk-Based Approach to Virtual Assets and Virtual Asset Service Providers*. Paris: FATF.

Financial Conduct Authority. (2019). *Guidance on Cryptoassets*. London: FCA.

International Organization of Securities Commissions. (2020). *Issues, Risks and Regulatory Considerations Relating to Crypto-Asset Trading Platforms*. Madrid: IOSCO.

Monetary Authority of Singapore. (2020). *Project Ubin: Central Bank Digital Money Using Distributed Ledger Technology*. Singapore: MAS.

UK Law Commission. (2021). *Smart Contracts: Call for Evidence*. London: Law Commission.

US Food and Drug Administration. (2019). *Drug Supply Chain Security Act (DSCSA) Implementation Plan*. Silver Spring: FDA.