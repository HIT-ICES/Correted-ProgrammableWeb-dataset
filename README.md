# Corrected ProgrammableWeb dataset

## Introduction

This repo contains the data and utils used in *Data Correction and Evolution Analysis of the ProgrammableWeb Service Ecosystem*.

Here is the content of each folder:

- `crawler`: The crawlers to get the data from ProgrammableWeb, including API crawler and Mashup crawler.
- `data`: The formatted datasets which are used in the paper are listed here. Its subfolder `raw` contains the raw data fetched by the crawlers in json type. 
- `visualization` folder contains some of the statistics results and visualization process.

## Data

We put our raw and corrected datasets in the `data` folder.

### Formatted Dataset

The raw data has been formatted in csv type. Some universal column names and their meanings are as follows:

| Column name | Meaning                      |
| ----------- | ---------------------------- |
| tp          | Type. API or Mashup          |
| url         | The URL of an API or Mashup  |
| name        | The API or Mashup's title    |
| st          | Submit date                  |
| et          | Corrected dead date          |
| oet         | Dead date provided in PW     |
| c           | Category                     |
| oac         | Corrected accessibility      |
| ac          | Accessibility provided in PW |

- `api_nodes_estimator.csv` is the API data. Each line represents an API.
- `m-a_edges.csv` is the data of Mashups invoking APIs.
- `mashup_nodes_estimator.csv` is the Mashup data.
- `split_nodes.csv` is the split API data.
- `transfer_nodes.csv` is the transferred API data.

### Raw data

- `active_apis_data.txt`, `deadpool_apis_data.txt`,  `active_mashups_data.txt`, `deadpool_mashups_data.txt`  are APIs and Mashups that are marked as active or dead on the ProgrammableWeb.
- `accessibility` subfolder contains APIs' accessibility and Mashups' accessibility. These data are collected by visiting the Homepage URL or API Endpoint or API Portal. With the dataset we can know if an service is still working.
- `all_pairs.txt`: A Mashup may invoke many APIs, and we collect the co-work APIs data and the frequencies as API pairs.


### Citation
If you make use of this code, we appreciate it if you can cite our paper as follows:
```
@article{liu2021data,
  title={Data correction and evolution analysis of the ProgrammableWeb service ecosystem},
  author={Liu, Mingyi and Tu, Zhiying and Zhu, Yeqi and Xu, Xiaofei and Wang, Zhongjie and Sheng, Quan Z},
  journal={Journal of Systems and Software},
  pages={111066},
  year={2021},
  publisher={Elsevier}
}
```
