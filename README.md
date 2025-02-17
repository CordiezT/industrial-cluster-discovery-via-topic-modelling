# Industrial Cluster Discovery via NLP
![Heatmap of Business Density](clusters-milton-keynes.png "Business Density Heatmap")

## Overview

Welcome to the repository for my master's thesis, **Industrial Cluster Discovery via NLP.** This project leverages Natural Language Processing (NLP) and Machine Learning (ML) techniques to analyze and cluster business activities within Milton Keynes. By extracting and analyzing textual data from company websites, we uncover valuable insights into the city's economic landscape, revealing hidden patterns and trends in industrial activities.

## Thesis Abstract

In this master's thesis, we delve into the discovery of industrial clusters in Milton Keynes by analyzing textual data from company websites. Using advanced NLP and ML techniques, we extract semantic information from the text, enabling us to perform clustering that highlights patterns and trends within the business landscape. This approach includes:

- **Data Collection**: Gathering and preprocessing web data to create a comprehensive dataset.
- **Geo-spatial Analysis**: Using Kernel Density Estimation (KDE) to map business activities and identify high-density areas.
- **NLP and ML Models**: Employing Latent Dirichlet Allocation (LDA) and BERTopic for robust topic modeling and clustering

My master's thesis investigates 5G business deployment opportunities in Milton Keynes through the application of large-scale natural language processing (NLP) and machine learning (ML) techniques to analyze textual data from company websites, enabling the identification of emerging industrial clusters with high commercial potential for 5G service adoption. Given that 5G infrastructure investment costs exceed $1.3 trillion globally by 2025, optimizing deployment requires precise sector-specific demand identification rather than blanket rollouts. This research addresses the challenge of mapping economic activity in real time, as traditional industrial classification systems such as Standard Industrial Classification (SIC) codes are often outdated, coarse-grained, and misaligned with modern business models. A major limitation of SIC codes is their static nature, failing to capture interdisciplinary firms and emerging industries such as AI-driven financial services or autonomous logistics, which demand ultra-reliable low-latency communications (URLLC) and massive machine-type communication (mMTC) capabilities. By applying unsupervised learning methods such as Latent Dirichlet Allocation (LDA) and BERTopic, the study extracts latent semantic structures from millions of words scraped from corporate websites, allowing the clustering of businesses into functional rather than administrative categories. The results are overlaid onto geospatial heatmaps using Kernel Density Estimation (KDE) to reveal business activity intensity zones, providing quantifiable recommendations for 5G network rollout and spectrum allocation.

Milton Keynes serves as an ideal testbed due to its status as a UK smart city prototype, where autonomous vehicle trials, IoT-based smart grid systems, and high-density logistics hubs already generate high bandwidth demand. Notable locations such as Red Bull Racing’s headquarters, the Milton Keynes Stadium, and high-tech business parks house companies reliant on ultra-low-latency networks for activities like real-time simulation, cloud-based design collaboration, and predictive maintenance analytics. The study employs a multi-stage data pipeline, beginning with the retrieval of over 22,000 company profiles via the Companies House API, followed by automated web scraping of business descriptions from corporate websites, geolocation processing via the Google Maps API, and text vectorization using Transformer-based embeddings such as BERT and Sentence-BERT (SBERT). Given that over 80% of corporate websites contain unstructured text, robust NLP preprocessing techniques including stopword removal, tokenization, lemmatization, and named entity recognition (NER) are applied to normalize descriptions and eliminate linguistic noise.

The ML pipeline utilizes TF-IDF vectorization combined with UMAP for dimensionality reduction, enabling scalable processing of over 1 million words per sector while preserving business-specific terminology. Clustering is performed using hierarchical density-based spatial clustering (HDBSCAN) and probabilistic topic models, with results evaluated using perplexity scores and coherence measures (Cv, UMass, and UCI metrics) to ensure interpretability. The study finds that a 14-topic BERTopic model achieves a coherence score of 0.45, significantly outperforming LDA’s 0.29, suggesting that transformer-based clustering is better suited for heterogeneous corporate text. Business clusters identified through NLP-based classification exhibit strong spatial correlations, reinforcing the notion that industry-specialized zones naturally emerge in cities through economic agglomeration effects, a concept widely recognized in urban economics.

Geospatial analytics reveals several high-density business activity hotspots, particularly within the western industrial corridor and city center, where businesses related to AI-driven financial services, precision manufacturing, and IoT-driven supply chain management are concentrated. Kernel Density Estimation (KDE) of business clusters shows that the top 10% most active business zones are 4.2 times denser than the median urban area, highlighting a strong case for prioritized 5G deployment in these regions. The study demonstrates that businesses engaged in logistics automation, smart manufacturing, and digital financial services form identifiable clusters, with FinTech-related businesses exhibiting a 37% higher likelihood of co-location near technology hubs. Such insights are crucial for targeting spectrum investments and optimizing fiber backhaul deployment, as they reveal where the highest data consumption demands will emerge.

From a computational perspective, the research addresses several key challenges inherent in large-scale NLP-driven industrial classification, including the high dimensionality of textual feature spaces, the difficulty of defining optimal clusters in unsupervised learning, and the need to balance clustering granularity with real-world interpretability. Unlike conventional k-means clustering, which assumes fixed cluster numbers and struggles with non-linearly separable data, BERTopic dynamically determines the number of industry clusters based on textual similarity, achieving an 8% reduction in intra-cluster variance compared to traditional TF-IDF-based methods. The study further explores graph-based clustering techniques such as Louvain community detection on company co-location networks, revealing that firms engaged in 5G-critical sectors exhibit modularity scores 24% higher than non-5G-relevant industries, indicating strong interconnectivity.

The broader implications of this research extend beyond 5G deployment, as the methodology provides a scalable, transferable framework for dynamic industrial mapping, offering decision-makers a continuously updating economic intelligence tool. The integration of NLP-derived industrial clusters with GIS-based business zoning strategies presents a replicable model for other smart cities seeking to optimize digital infrastructure planning. Future work includes incorporating multi-modal datasets such as financial transaction records and IoT sensor data to enhance predictive capabilities, refining graph-based clustering to capture inter-business dependencies, and developing a real-time dashboard for policymakers to monitor economic shifts in urban environments. By demonstrating that NLP-driven industrial classification can provide real-time, high-resolution insights into economic activity, this research contributes to the advancement of AI-enhanced urban planning, reinforcing the necessity of data-driven approaches to shaping the future of digital connectivity, infrastructure development, and smart city governance.

## Key Components

### Data Collection
- **APIs and Web Scraping**: Utilizing Companies House API, GoogleMaps API, and web scraping tools to collect and preprocess textual data from company websites.
- **Comprehensive Dataset**: Building a rich dataset that captures the diverse business activities within Milton Keynes.

### Geo-spatial Analysis
- **Density Mapping**: Creating density maps to visualize the concentration of business activities.
- **Cluster Identification**: Identifying clusters of business activities that reveal economic hotspots and potential areas for development.

### NLP and ML Models
- **Latent Dirichlet Allocation (LDA)**: Implementing LDA to extract topics and uncover underlying themes in the textual data.
- **BERTopic**: Using transformer-based clustering to enhance the accuracy and interpretability of the clusters.

### Visualization
- **Interactive Maps**: Visualizing business clusters on interactive maps, highlighting various sectors and their distribution across the city.
- **Insightful Graphics**: Providing compelling visualizations that make the findings easy to understand and explore.

## Results

### Discoveries and Insights
- **Economic Hotspots**: Identified high-density areas of business activities, highlighting key economic hotspots within Milton Keynes.
- **Sector Distribution**: Mapped the distribution of various business sectors, providing insights into the city's industrial landscape.
- **Strategic Development**: Offered valuable data-driven insights that can guide urban planning and development strategies, fostering a smarter and more efficient city.
