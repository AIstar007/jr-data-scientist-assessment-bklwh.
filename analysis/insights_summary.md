<class 'pandas.core.frame.DataFrame'>
Int64Index: 96 entries, 0 to 95
Data columns (total 36 columns):
 #   Column                 Non-Null Count  Dtype  
---  ------                 --------------  -----  
 0   patient_id             96 non-null     object 
 1   ht                     96 non-null     int64  
 2   wt                     96 non-null     float64
 3   education              96 non-null     int64  
 4   income                 96 non-null     int64  
 5   ageatmenarche          96 non-null     int64  
 6   ageatmarriage          96 non-null     int64  
 7   ageatfirstpregnancy    96 non-null     int64  
 8   district               96 non-null     object 
 9   village                96 non-null     object 
 10  occupation             96 non-null     object 
 11  diet                   96 non-null     object 
 12  condition              96 non-null     object 
 13  dateofdelivery         96 non-null     object 
 14  ageatdelivery          96 non-null     int64  
 15  weightatdelivery       96 non-null     float64
 16  haemoglobinatdelivery  96 non-null     float64
 17  placentalweight        96 non-null     int64  
 18  termofdelivery         96 non-null     object 
 19  typeofdelivery         96 non-null     object 
 20  Visit1_bpdis           96 non-null     int64  
 21  Visit1_bpsys           96 non-null     int64  
 22  Visit1_date            96 non-null     object 
 23  Visit1_wt              96 non-null     float64
 24  Visit2_bpdis           96 non-null     int64  
 25  Visit2_bpsys           96 non-null     int64  
 26  Visit2_date            96 non-null     object 
 27  Visit2_wt              96 non-null     float64
 28  Visit3_bpdis           96 non-null     int64  
 29  Visit3_bpsys           96 non-null     int64  
 30  Visit3_date            96 non-null     object 
 31  Visit3_wt              96 non-null     float64
 32  Visit4_bpdis           96 non-null     int64  
 33  Visit4_bpsys           96 non-null     int64  
 34  Visit4_date            96 non-null     object 
 35  Visit4_wt              96 non-null     float64
dtypes: float64(7), int64(16), object(13)
memory usage: 27.8+ KB
Result
(None,
        patient_id          ht         wt  education        income  \
 count          96   96.000000  96.000000  96.000000     96.000000   
 unique         96         NaN        NaN        NaN           NaN   
 top            P1         NaN        NaN        NaN           NaN   
 freq            1         NaN        NaN        NaN           NaN   
 mean          NaN  151.729167  53.564583  10.708333  13906.250000   
 std           NaN    6.452220  12.249702   2.470528   6212.175015   
 min           NaN  135.000000  28.700000   4.000000   1000.000000   
 25%           NaN  148.000000  43.400000   9.750000  10000.000000   
 50%           NaN  152.000000  53.800000  12.000000  11000.000000   
 75%           NaN  156.000000  60.800000  12.000000  18000.000000   
 max           NaN  175.000000  90.000000  15.000000  30000.000000   
 
         ageatmenarche  ageatmarriage  ageatfirstpregnancy   district  \
 count       96.000000      96.000000            96.000000         96   
 unique            NaN            NaN                  NaN          8   
 top               NaN            NaN                  NaN  Ratnagiri   
 freq              NaN            NaN                  NaN         33   
 mean        13.375000      22.729167            24.479167        NaN   
 std          1.241815       2.870830             3.393428        NaN   
 min         10.000000      17.000000            18.000000        NaN   
 25%         13.000000      20.000000            22.000000        NaN   
 50%         13.000000      23.000000            24.000000        NaN   
 75%         14.000000      25.000000            27.000000        NaN   
 max         19.000000      30.000000            33.000000        NaN   
 
          village  ... Visit2_date  Visit2_wt Visit3_bpdis Visit3_bpsys  \
 count         96  ...          96  96.000000    96.000000    96.000000   
 unique        11  ...          88        NaN          NaN          NaN   
 top     Kankavli  ...  2023-04-25        NaN          NaN          NaN   
 freq          14  ...           2        NaN          NaN          NaN   
 mean         NaN  ...         NaN  54.299167    70.145833   107.854167   
 std          NaN  ...         NaN  12.006902     8.822196    12.119562   
 min          NaN  ...         NaN  31.600000    50.000000    80.000000   
 25%          NaN  ...         NaN  44.450000    60.000000   100.000000   
 50%          NaN  ...         NaN  53.600000    70.000000   110.000000   
 75%          NaN  ...         NaN  62.025000    70.000000   110.000000   
 max          NaN  ...         NaN  89.300000    90.000000   150.000000   
 
         Visit3_date  Visit3_wt  Visit4_bpdis  Visit4_bpsys Visit4_date  \
 count            96  96.000000     96.000000     96.000000          96   
 unique           92        NaN           NaN           NaN          83   
 top      2023-07-06        NaN           NaN           NaN  2023-11-18   
 freq              2        NaN           NaN           NaN           3   
 mean            NaN  55.674479     71.041667    109.583333         NaN   
 std             NaN  12.136209      9.231430     13.862229         NaN   
 min             NaN  35.000000     50.000000     80.000000         NaN   
 25%             NaN  45.000000     67.500000    100.000000         NaN   
 50%             NaN  55.400000     70.000000    110.000000         NaN   
 75%             NaN  62.050000     80.000000    120.000000         NaN   
 max             NaN  92.700000    100.000000    170.000000         NaN   
 
         Visit4_wt  
 count   96.000000  
 unique        NaN  
 top           NaN  
 freq          NaN  
 mean    57.383021  
 std     12.472000  
 min     35.000000  
 25%     46.525000  
 50%     57.450000  
 75%     65.000000  
 max     99.900000  
 
 [11 rows x 36 columns])
