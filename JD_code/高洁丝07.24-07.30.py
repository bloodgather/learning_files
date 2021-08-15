#!/usr/bin/env python
# coding: utf-8

# In[1]:


tool_week = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/ef6b2d5af1ac11eb9991fa163e446b35.csv')
pinlei_ttl_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/6cd0e698f1a511eb9a06fa163eb774d5.csv')
gjs_allsku_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/1ff7a668f1a511eb9f6afa163eb774d5.csv')
gjs_allsku_pre11m_monthly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/55581a4ce2b711eba678fa163eb774d5.csv')
gjs_allsku_pre11m_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/5eb07154efad11eb8240fa163e446b35.csv')
gjs_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/ae827244f1a711eb9b7ffa163eb774d5.csv')
hsb_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/a4b54476f1a711eb9a06fa163eb774d5.csv')
sf_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/36ba5294f1ad11ebad02fa163eb774d5.csv')
qdkj_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/4ddc23def1a911eb9a06fa163eb774d5.csv')
ley_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/a4c00f46f1a711eb9991fa163e446b35.csv')
pinlei_ttl_uv_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/2ea8fa96f1a911ebad02fa163eb774d5.csv')
gjs_uv_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/fb24603cf1aa11eba678fa163eb774d5.csv')
hsb_uv_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/24f5b236f1aa11ebbb35fa163eb774d5.csv')
sf_uv_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/2518eeaef1aa11eba678fa163eb774d5.csv')
qdkj_uv_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/fb358cf4f1aa11eb8240fa163e446b35.csv')
ley_uv_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/b384e486f1aa11eb8c97fa163e446b35.csv')
gjs_pre11m_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/c5726fccefae11eb8c97fa163e446b35.csv')
hsb_pre11m_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/c3c3fb0aefae11eb93b1fa163e446b35.csv')
sf_pre11m_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/0aadc87aefaf11eb9991fa163e446b35.csv')
qdkj_pre11m_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/9a32976eefaf11eb9991fa163e446b35.csv')
ley_pre11m_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/c54bcf0cefae11eb8f7afa163e446b35.csv')
pinlei_nokx_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/07611c3ef1a911eb8f7afa163e446b35.csv')
gjs_nokx_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/278a96e2f1aa11eb9a06fa163eb774d5.csv')
hsb_nokx_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/e426f29cf1ae11eb8c97fa163e446b35.csv')
sf_nokx_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/6db36d24f1aa11ebb876fa163eb774d5.csv')
qdkj_nokx_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/6dd4db1cf1aa11eb8240fa163e446b35.csv')
ley_nokx_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/e699f8eef1ae11eb93b1fa163e446b35.csv')
pinlei_nokx_uv_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/95f96032f1a911eb9b7ffa163eb774d5.csv')
gjs_nokx_uv_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/5528b2f6f1ae11ebad02fa163eb774d5.csv')
hsb_nokx_uv_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/733b29b2f1af11ebad02fa163eb774d5.csv')
sf_nokx_uv_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/fb85bbacf1aa11eb9991fa163e446b35.csv')
qdkj_nokx_uv_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/75af1d20f1af11eb8c97fa163e446b35.csv')
ley_nokx_uv_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/42fb104af1ab11ebb876fa163eb774d5.csv')
pinlei_ttl_cust_kx_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/ddcba46af1a911eb940bfa163e446b35.csv')
gjs_cust_kx_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/7e44702cf1ad11eb940bfa163e446b35.csv')
hsb_cust_kx_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/6dfac08ef1aa11eba678fa163eb774d5.csv')
sf_cust_kx_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/b38f2068f1aa11eb9a06fa163eb774d5.csv')
qdkj_cust_kx_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/fb24743cf1aa11eb8786fa163eb774d5.csv')
ley_cust_kx_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/fd9498aaf1aa11eb8240fa163e446b35.csv')
pinlei_ttl_uv_kx_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/6e65203cf1aa11eb8c97fa163e446b35.csv')
gjs_uv_kx_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/7e55afccf1ad11ebad02fa163eb774d5.csv')
hsb_uv_kx_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/c5c8d708f1ad11ebb876fa163eb774d5.csv')
sf_uv_kx_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/001c839ef1ab11eb8c97fa163e446b35.csv')
qdkj_uv_kx_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/54dcb2f2f1ae11ebb876fa163eb774d5.csv')
ley_uv_kx_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/fcc5368cf1aa11eb8f7afa163e446b35.csv')
pinlei_nokx_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/07611c3ef1a911eb8f7afa163e446b35.csv')
gjs_nokx_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/278a96e2f1aa11eb9a06fa163eb774d5.csv')
pinlei_nokx_uv_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/95f96032f1a911eb9b7ffa163eb774d5.csv')
gjs_nokx_uv_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/5528b2f6f1ae11ebad02fa163eb774d5.csv')
gjs_zx_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/fba632baf1aa11eb8f7afa163e446b35.csv')
gjs_snj_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/ff2df6acf1aa11eb9f6afa163eb774d5.csv')
gjs_zxb_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/fdfdb3bcf1aa11eb8240fa163e446b35.csv')
#N/A
gjs_yak_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/b3a8160ef1aa11eb8786fa163eb774d5.csv')
gjs_zx_uv_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/d148d878f1ab11eb940bfa163e446b35.csv')
gjs_snj_uv_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/d140f8d8f1ab11ebbd3efa163e446b35.csv')
gjs_zxb_uv_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/d17ec172f1ab11eb9a06fa163eb774d5.csv')
gjs_nature_uv_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/d19b5fa8f1ab11ebbb35fa163eb774d5.csv')
gjs_yak_uv_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/d1ac061ef1ab11eb9baefa163e446b35.csv')
gjs_zx_cust_hg_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/01153426f1ab11eb93b1fa163e446b35.csv')
gjs_nature_cust_weekly_bing = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/e4e50b06f1ae11ebad02fa163eb774d5.csv')

gjs_zx_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/fba632baf1aa11eb8f7afa163e446b35.csv')
gjs_fss_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/b3bbffd4f1aa11eb940bfa163e446b35.csv')
gjs_jtk_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/fdb425a8f1aa11eba678fa163eb774d5.csv')
gjs_yak_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/b3a8160ef1aa11eb8786fa163eb774d5.csv')
gjs_snj_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/ff2df6acf1aa11eb9f6afa163eb774d5.csv')
#N/A
#N/A
gjs_sf_gd_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/9c4bd9a6f1ae11ebbb35fa163eb774d5.csv')
gjs_hsb_gd_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/14ba619cf1b311eb9a06fa163eb774d5.csv')
gjs_hzm_cust_weekly_bing = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/e457e028f1ae11eb9b7ffa163eb774d5.csv')
gjs_ysas_cust_mtd = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/5bbfa1b2f1a711eba678fa163eb774d5.csv')

gjs_hdm_uv_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/45676522f1ab11eb8240fa163e446b35.csv')
#N/A
gjs_hdm_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/439e4e68f1ab11eb9f6afa163eb774d5.csv')
gjs_hdm_search_weekly_bing = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/2bacd47ef1af11eb9baefa163e446b35.csv')
#N/A
gjs_ysas_cust_weekly = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/ce73bb22f1a611eb8786fa163eb774d5.csv')
gjs_snj_cust_weekly_tichuqian = spark.read.format("org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").option("header","true").option("inferSchema","false").option("delimiter",",").load('s3a://bde05811429afe725277ae5a5eff136b/readonly/sf/449007a8f1ab11eb940bfa163e446b35.csv')


# In[2]:


gjs_hdm_search_weekly=gjs_hdm_search_weekly_bing.subtract(tool_week)
gjs_hzm_cust_weekly=gjs_hzm_cust_weekly_bing.subtract(tool_week)

gjs_nature_cust_weekly=gjs_nature_cust_weekly_bing.subtract(tool_week)


pinlei_ttl_cust_weekly=pinlei_ttl_cust_weekly.subtract(gjs_ysas_cust_weekly)
gjs_allsku_cust_weekly=gjs_allsku_cust_weekly.subtract(gjs_ysas_cust_weekly)
gjs_cust_weekly=gjs_cust_weekly.subtract(gjs_ysas_cust_weekly)
pinlei_nokx_cust_weekly=pinlei_nokx_cust_weekly.subtract(gjs_ysas_cust_weekly)
gjs_nokx_cust_weekly=gjs_nokx_cust_weekly.subtract(gjs_ysas_cust_weekly)
pinlei_ttl_cust_kx_weekly=pinlei_ttl_cust_kx_weekly.subtract(gjs_ysas_cust_weekly)
gjs_cust_kx_weekly=gjs_cust_kx_weekly.subtract(gjs_ysas_cust_weekly)

gjs_allsku_pre11m_monthly=gjs_allsku_pre11m_monthly.subtract(gjs_ysas_cust_mtd)
gjs_allsku_pre11m_weekly=gjs_allsku_pre11m_weekly.subtract(gjs_ysas_cust_mtd)
gjs_pre11m_weekly=gjs_pre11m_weekly.subtract(gjs_ysas_cust_mtd)


# In[3]:


# ===============================================
###近一周TTL用户及UV
# ===============================================

List3 = [
#品类用户(卫生巾+女性护理套装+裤型)
pinlei_ttl_cust_weekly,
#高洁丝用户
gjs_cust_weekly,
#护舒宝用户
hsb_cust_weekly,
#苏菲用户
sf_cust_weekly,
#七度空间用户
qdkj_cust_weekly,
#乐而雅用户
ley_cust_weekly,
#品类总UV
pinlei_ttl_uv_weekly,
#高洁丝UV 
gjs_uv_weekly,
#护舒宝UV
hsb_uv_weekly,
#苏菲UV
sf_uv_weekly,
#七度空间UV
qdkj_uv_weekly,
#乐而雅UV
ley_uv_weekly,
#高洁丝新客
gjs_cust_weekly.subtract(gjs_pre11m_weekly),
#护舒宝新客
hsb_cust_weekly.subtract(hsb_pre11m_weekly),
#苏菲新客
sf_cust_weekly.subtract(sf_pre11m_weekly),
#七度空间新客
qdkj_cust_weekly.subtract(qdkj_pre11m_weekly),
#乐而雅新客
ley_cust_weekly.subtract(ley_pre11m_weekly),
#高洁丝新客UV
gjs_uv_weekly.subtract(gjs_pre11m_weekly),
#护舒宝新客UV
hsb_uv_weekly.subtract(hsb_pre11m_weekly),
#苏菲新客UV 
sf_uv_weekly.subtract(sf_pre11m_weekly),
#七度空间新客UV###
qdkj_uv_weekly.subtract(qdkj_pre11m_weekly),
#乐而雅新客UV
ley_uv_weekly.subtract(ley_pre11m_weekly),
#高洁丝老客
gjs_cust_weekly.intersect(gjs_pre11m_weekly),
#护舒宝老客
hsb_cust_weekly.intersect(hsb_pre11m_weekly),
#苏菲老客
sf_cust_weekly.intersect(sf_pre11m_weekly),
#七度空间老客
qdkj_cust_weekly.intersect(qdkj_pre11m_weekly),
#乐而雅老客
ley_cust_weekly.intersect(ley_pre11m_weekly),
#高洁丝老客UV
gjs_uv_weekly.intersect(gjs_pre11m_weekly),
#护舒宝老客UV
hsb_uv_weekly.intersect(hsb_pre11m_weekly),
#苏菲老客UV
sf_uv_weekly.intersect(sf_pre11m_weekly),
#七度空间老客UV
qdkj_uv_weekly.intersect(qdkj_pre11m_weekly),
#乐而雅老客UV
ley_uv_weekly.intersect(ley_pre11m_weekly),
]

for i in List3:
    print(i.distinct().count())


# In[4]:


# ===============================================
###近一周卫生巾&护理套装用户及UV 
# ===============================================

List4 = [
#品类用户(卫生巾+女性护理套装)
pinlei_nokx_cust_weekly,
#高洁丝用户
gjs_nokx_cust_weekly,
#护舒宝用户
hsb_nokx_cust_weekly,
#苏菲用户
sf_nokx_cust_weekly,
#七度空间用户
qdkj_nokx_cust_weekly,
#乐而雅用户
ley_nokx_cust_weekly,
#品类总UV
pinlei_nokx_uv_weekly,
#高洁丝UV 
gjs_nokx_uv_weekly,
#护舒宝UV
hsb_nokx_uv_weekly,
#苏菲UV
sf_nokx_uv_weekly,
#七度空间UV
qdkj_nokx_uv_weekly,
#乐而雅UV
ley_nokx_uv_weekly,
#高洁丝新客
gjs_nokx_cust_weekly.subtract(gjs_pre11m_weekly),
#护舒宝新客
hsb_nokx_cust_weekly.subtract(hsb_pre11m_weekly),
#苏菲新客
sf_nokx_cust_weekly.subtract(sf_pre11m_weekly),
#七度空间新客
qdkj_nokx_cust_weekly.subtract(qdkj_pre11m_weekly),
#乐而雅新客
ley_nokx_cust_weekly.subtract(ley_pre11m_weekly),
#高洁丝新客UV
gjs_nokx_uv_weekly.subtract(gjs_pre11m_weekly),
#护舒宝新客UV 19
hsb_nokx_uv_weekly.subtract(hsb_pre11m_weekly),
#苏菲新客UV 
sf_nokx_uv_weekly.subtract(sf_pre11m_weekly),
#七度空间新客UV
qdkj_nokx_uv_weekly.subtract(qdkj_pre11m_weekly),
#乐而雅老客UV
ley_nokx_uv_weekly.subtract(ley_pre11m_weekly),
#高洁丝老客
gjs_nokx_cust_weekly.intersect(gjs_pre11m_weekly),
#护舒宝老客
hsb_nokx_cust_weekly.intersect(hsb_pre11m_weekly),
#苏菲老客
sf_nokx_cust_weekly.intersect(sf_pre11m_weekly),
#七度空间老客
qdkj_nokx_cust_weekly.intersect(qdkj_pre11m_weekly),
#乐而雅老客
ley_nokx_cust_weekly.intersect(ley_pre11m_weekly),
#高洁丝老客UV
gjs_nokx_uv_weekly.intersect(gjs_pre11m_weekly),
#护舒宝老客UV
hsb_nokx_uv_weekly.intersect(hsb_pre11m_weekly),
#苏菲老客UV
sf_nokx_uv_weekly.intersect(sf_pre11m_weekly),
#七度空间老客UV
qdkj_nokx_uv_weekly.intersect(qdkj_pre11m_weekly),
#乐而雅老客UV
ley_nokx_uv_weekly.intersect(ley_pre11m_weekly),
]

for i in List4:
    print(i.distinct().count())


# In[5]:


# ===============================================
###近一周裤型卫生巾用户及UV
# ===============================================

List5 = [
#品类用户(裤型)
pinlei_ttl_cust_kx_weekly,
#高洁丝用户
gjs_cust_kx_weekly,
#护舒宝用户
hsb_cust_kx_weekly,
#苏菲用户
sf_cust_kx_weekly,
#七度空间用户
qdkj_cust_kx_weekly,
#乐而雅用户
ley_cust_kx_weekly,
#品类总UV
pinlei_ttl_uv_kx_weekly,
#高洁丝UV 
gjs_uv_kx_weekly,
#护舒宝UV
hsb_uv_kx_weekly,
#苏菲UV
sf_uv_kx_weekly,
#七度空间UV
qdkj_uv_kx_weekly,
#乐而雅UV
ley_uv_kx_weekly,
#高洁丝新客
gjs_cust_kx_weekly.subtract(gjs_pre11m_weekly),
#护舒宝新客
hsb_cust_kx_weekly.subtract(hsb_pre11m_weekly),
#苏菲新客
sf_cust_kx_weekly.subtract(sf_pre11m_weekly),
#七度空间新客
qdkj_cust_kx_weekly.subtract(qdkj_pre11m_weekly),
#乐而雅新客
ley_cust_kx_weekly.subtract(ley_pre11m_weekly),
#高洁丝新客UV
gjs_uv_kx_weekly.subtract(gjs_pre11m_weekly),
#护舒宝新客UV
hsb_uv_kx_weekly.subtract(hsb_pre11m_weekly),
#苏菲新客UV
sf_uv_kx_weekly.subtract(sf_pre11m_weekly),
#七度空间新客UV
qdkj_uv_kx_weekly.subtract(qdkj_pre11m_weekly),
#乐而雅新客UV
ley_uv_kx_weekly.subtract(ley_pre11m_weekly),
#高洁丝老客
gjs_cust_kx_weekly.intersect(gjs_pre11m_weekly),
#护舒宝老客
hsb_cust_kx_weekly.intersect(hsb_pre11m_weekly),
#苏菲老客
sf_cust_kx_weekly.intersect(sf_pre11m_weekly),
#七度空间老客
qdkj_cust_kx_weekly.intersect(qdkj_pre11m_weekly),
#乐而雅老客
ley_cust_kx_weekly.intersect(ley_pre11m_weekly),
#高洁丝老客UV
gjs_uv_kx_weekly.intersect(gjs_pre11m_weekly),
#护舒宝老客UV
hsb_uv_kx_weekly.intersect(hsb_pre11m_weekly),
#苏菲老客UV
sf_uv_kx_weekly.intersect(sf_pre11m_weekly),
#七度空间老客UV
qdkj_uv_kx_weekly.intersect(qdkj_pre11m_weekly),
#乐而雅老客UV
ley_uv_kx_weekly.intersect(ley_pre11m_weekly),
]

for i in List5:
    print(i.distinct().count())


# In[12]:


#### ===============================================
###臻选VS竞品追踪
# ===============================================

List2 = [
#品类用户(卫生巾+女性护理套装)
pinlei_nokx_cust_weekly,
#高洁丝用户all sku
gjs_allsku_cust_weekly,
#臻选用户
gjs_zx_cust_weekly,
#少女肌用户
gjs_snj_cust_weekly,
#爪心包用户
gjs_zxb_cust_weekly,
#Nature用户

gjs_nature_cust_weekly,
    
#夜安裤用户
gjs_yak_cust_weekly,
#海岛棉用户
gjs_hdm_cust_weekly,
#品类总 UV
pinlei_nokx_uv_weekly,
#高洁丝TTLUV
gjs_nokx_uv_weekly,
#臻选UV
gjs_zx_uv_weekly,
#少女肌UV
gjs_snj_uv_weekly,
#爪心包UV
gjs_zxb_uv_weekly,
#NatureUV
gjs_nature_uv_weekly,
#夜安裤UV
gjs_yak_uv_weekly,
#海岛棉UV
gjs_hdm_uv_weekly,
#高洁丝TTL新客
gjs_allsku_cust_weekly.subtract(gjs_allsku_pre11m_weekly),
#臻选新客
gjs_zx_cust_weekly.subtract(gjs_allsku_pre11m_weekly),
#少女肌新客
gjs_snj_cust_weekly.subtract(gjs_allsku_pre11m_weekly),
#爪心包新客
gjs_zxb_cust_weekly.subtract(gjs_allsku_pre11m_weekly),
#Nature新客
    
gjs_nature_cust_weekly.subtract(gjs_allsku_pre11m_weekly),
    
#夜安裤新客
gjs_yak_cust_weekly.subtract(gjs_allsku_pre11m_weekly),
#海岛棉新客
gjs_hdm_cust_weekly.subtract(gjs_allsku_pre11m_weekly),

#高洁丝TTL新客UV
gjs_nokx_uv_weekly.subtract(gjs_allsku_pre11m_weekly),
#臻选新客UV
gjs_zx_uv_weekly.subtract(gjs_allsku_pre11m_weekly),
#少女肌新客UV
gjs_snj_uv_weekly.subtract(gjs_allsku_pre11m_weekly),
#爪心包新客UV
gjs_zxb_uv_weekly.subtract(gjs_allsku_pre11m_weekly),
#Nature新客UV
gjs_nature_uv_weekly.subtract(gjs_allsku_pre11m_weekly),
#夜安裤新客UV
gjs_yak_uv_weekly.subtract(gjs_allsku_pre11m_weekly),
#海岛棉新客UV
gjs_hdm_uv_weekly.subtract(gjs_allsku_pre11m_weekly),
#高洁丝TTL老客
gjs_allsku_cust_weekly.intersect(gjs_allsku_pre11m_weekly),
#臻选老客
gjs_zx_cust_weekly.intersect(gjs_allsku_pre11m_weekly),
#少女肌老客
gjs_snj_cust_weekly.intersect(gjs_allsku_pre11m_weekly),
#爪心包老客
gjs_zxb_cust_weekly.intersect(gjs_allsku_pre11m_weekly),
#Nature老客
    
gjs_nature_cust_weekly.intersect(gjs_allsku_pre11m_weekly),
    
#夜安裤老客
gjs_yak_cust_weekly.intersect(gjs_allsku_pre11m_weekly),
#海岛棉老客
gjs_hdm_cust_weekly.intersect(gjs_allsku_pre11m_weekly),


#高洁丝TTL老客UV
gjs_nokx_uv_weekly.intersect(gjs_allsku_pre11m_weekly),
#臻选老客UV
gjs_zx_uv_weekly.intersect(gjs_allsku_pre11m_weekly),
#少女肌老客UV ####
gjs_snj_uv_weekly.intersect(gjs_allsku_pre11m_weekly),
#爪心包老客UV
gjs_zxb_uv_weekly.intersect(gjs_allsku_pre11m_weekly),
#Nature老客UV
gjs_nature_uv_weekly.intersect(gjs_allsku_pre11m_weekly),
#夜安裤老客UV
gjs_yak_uv_weekly.intersect(gjs_allsku_pre11m_weekly),
#海岛棉老客UV
gjs_hdm_uv_weekly.intersect(gjs_allsku_pre11m_weekly)
]

for i in List2:
    print(i.distinct().count())


# In[7]:


List6=[
#品类总UV
pinlei_ttl_uv_kx_weekly,
#高洁丝UV 
gjs_uv_kx_weekly,
#护舒宝UV
hsb_uv_kx_weekly,
#苏菲UV
sf_uv_kx_weekly,
#七度空间UV
qdkj_uv_kx_weekly,
#乐而雅UV
ley_uv_kx_weekly]

for i in List6:
    print(i.distinct().count())


# In[8]:


#京挑客点击
List_jtk=[gjs_zx_cust_weekly,gjs_yak_cust_weekly,gjs_snj_cust_weekly_tichuqian,
          gjs_fss_cust_weekly,gjs_nature_cust_weekly,gjs_hzm_cust_weekly,
          gjs_zxb_cust_weekly,gjs_hdm_cust_weekly]
print(gjs_jtk_cust_weekly.distinct().count())
j=gjs_jtk_cust_weekly.intersect(gjs_allsku_cust_weekly)
k=gjs_jtk_cust_weekly.intersect(gjs_allsku_cust_weekly).subtract(gjs_pre11m_weekly)
print(j.distinct().count())
print(k.distinct().count())

for i in List_jtk:
    j=gjs_jtk_cust_weekly.intersect(i)
    k=gjs_jtk_cust_weekly.intersect(i).subtract(gjs_pre11m_weekly)
    print(j.distinct().count())
    print(k.distinct().count())


# In[9]:


#高端品
gjs_gd_cust_weekly=gjs_nature_cust_weekly.union(gjs_hdm_cust_weekly)
List_gd=[gjs_gd_cust_weekly,gjs_sf_gd_weekly,
         gjs_hsb_gd_weekly,ley_cust_weekly]
for i in List_gd:
    print(i.distinct().count())


# In[10]:


#海岛棉
print(gjs_hdm_cust_weekly.distinct().count())
print(gjs_hdm_search_weekly.distinct().count())


# In[11]:


print(gjs_zx_cust_hg_weekly.distinct().count())


# In[ ]:




