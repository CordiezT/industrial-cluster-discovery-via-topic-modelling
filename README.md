# **5G Business Opportunities in Milton Keynes: A Geo-Spatial NLP Approach**  

![Heatmap of Business Density](clusters-milton-keynes.png "Business Density Heatmap")  

## **Overview**  

This study investigates **5G business deployment opportunities** in **Milton Keynes** through **large-scale natural language processing (NLP) and machine learning (ML)** techniques, analyzing textual data from company websites to identify **emerging industrial clusters** with high commercial potential for **5G service adoption**. Given that **5G infrastructure investment costs are projected to exceed $1.3 trillion globally by 2025**, optimizing deployment requires **sector-specific demand identification** rather than blanket rollouts.  

Traditional industrial classification systems such as [**Standard Industrial Classification (SIC) codes**](https://www.ons.gov.uk/methodology/classificationsandstandards/ukstandardindustrialclassificationofeconomicactivities) are often outdated, coarse-grained, and misaligned with modern business models. **SIC codes fail to capture interdisciplinary firms and emerging industries** such as **AI-driven financial services** or **autonomous logistics**, both of which demand **ultra-reliable low-latency communications (URLLC)** and **massive machine-type communication (mMTC)** capabilities.  

By applying **unsupervised learning methods** such as [**Latent Dirichlet Allocation (LDA)**](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation) and [**BERTopic**](https://maartengr.github.io/BERTopic/), the study extracts **latent semantic structures from millions of words**, allowing businesses to be **clustered based on function rather than administrative categories**. The results are overlaid onto **geospatial heatmaps** using [**Kernel Density Estimation (KDE)**](https://en.wikipedia.org/wiki/Kernel_density_estimation) to reveal **business activity intensity zones**, providing **quantifiable recommendations for 5G network rollout and spectrum allocation**.  

## **Why Milton Keynes?**  

Milton Keynes serves as an **ideal testbed** due to its **status as a UK smart city prototype**, where **autonomous vehicle trials, IoT-based smart grid systems, and high-density logistics hubs already generate high bandwidth demand**. Notable locations such as **Red Bull Racing's headquarters**, **Milton Keynes Stadium**, and high-tech business parks house companies that rely on **ultra-low-latency networks** for activities such as **real-time simulation, cloud-based design collaboration, and predictive maintenance analytics**.  

## **Data Pipeline and NLP Processing**  

The study employs a **multi-stage data pipeline**, beginning with the **retrieval of over 22,000 company profiles via the [Companies House API](https://developer.company-information.service.gov.uk/)**, followed by **automated web scraping of business descriptions**, **geolocation processing via the [Google Maps API](https://developers.google.com/maps/documentation/places/web-service/overview)**, and **text vectorization using Transformer-based embeddings** such as [**BERT**](https://en.wikipedia.org/wiki/BERT_(language_model)) and [**SBERT**](https://www.sbert.net/).  

Given that **over 80% of corporate websites contain unstructured text**, robust **NLP preprocessing techniques** (including **stopword removal, tokenization, lemmatization, and named entity recognition (NER)**) are applied to normalize descriptions and eliminate linguistic noise.  

The ML pipeline utilizes **TF-IDF vectorization combined with [UMAP](https://umap-learn.readthedocs.io/en/latest/) for dimensionality reduction**, enabling scalable processing of **over 1 million words per sector** while preserving **business-specific terminology**. Clustering is performed using **hierarchical density-based spatial clustering ([HDBSCAN](https://hdbscan.readthedocs.io/en/latest/)) and probabilistic topic models**, with results evaluated using **perplexity scores and coherence measures (Cv, UMass, and UCI metrics)** to ensure interpretability. The study finds that a **14-topic BERTopic model achieves a coherence score of 0.45, significantly outperforming LDA’s 0.29**, suggesting that transformer-based clustering is better suited for heterogeneous corporate text.  

## **Geo-Spatial Insights and Business Clusters**  

The integration of **geospatial analytics** ensures that **NLP-extracted business clusters** are **both semantically relevant and geographically coherent**, enabling precise targeting of **5G infrastructure deployment** in areas with **the highest economic density and projected network demand**. KDE mapping of NLP-generated clusters reveals **that the top 10% most active business zones are 4.2 times denser than the median urban area**, strongly supporting **targeted 5G deployment strategies**.  

## **Computational and ML Challenges**  

The research tackles several challenges inherent in **large-scale NLP-driven industrial classification**, including:  

- **High dimensionality of textual feature spaces**, requiring **advanced dimensionality reduction techniques** to maintain performance.  
- **Defining optimal clusters in unsupervised learning**, particularly when business descriptions contain ambiguous terminology.  
- **Balancing clustering granularity with real-world interpretability**, as increasing cluster count improves specificity but risks over-segmentation.  

Unlike **k-means clustering**, which assumes a **fixed number of clusters** and struggles with **non-linearly separable data**, BERTopic dynamically determines the **optimal number of industry clusters** based on textual similarity, achieving an **8% reduction in intra-cluster variance compared to traditional TF-IDF-based methods**. The study also explores **graph-based clustering techniques** such as **Louvain community detection** ([a widely used graph partitioning method](https://en.wikipedia.org/wiki/Louvain_method)) on company co-location networks.  

## **Strategic Implications and Future Work**  

Beyond **5G deployment**, the research provides a **scalable and transferable framework for real-time economic intelligence**, offering an **automated system for continuously updating business sector classifications**. Future research will incorporate **multi-modal datasets** such as **financial transaction records and IoT sensor data**, refine **graph-based clustering to capture inter-business dependencies**, and **develop a real-time AI-powered dashboard for policymakers** to monitor **economic shifts and network demand forecasting**.  

## **Conclusion**  

By demonstrating that **NLP-driven industrial classification** can provide **real-time, high-resolution insights into economic activity**, this research contributes to **AI-enhanced urban planning** and reinforces the **necessity of data-driven methodologies** in shaping **the future of digital connectivity, infrastructure development, and smart city governance**. The application of **transformer-based text analytics**, combined with **geospatial modeling**, proves to be an effective tool for **dynamic business mapping**, highlighting **previously unseen economic clusters** and enabling **precise, cost-effective 5G deployment strategies**.  

## **Thesis Document**  
📄 **[Download Full Thesis (PDF)](docs/TheophileCordiez_Master_Thesis_340169.pdf)**  

