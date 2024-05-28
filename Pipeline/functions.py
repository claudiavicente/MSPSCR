import numpy as np
from scipy import stats
from statsmodels.stats import multitest
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import hypergeom

########################################################################################################################################

def flux_transformer(v):

    def adjusted(v):
        new = (np.log2(v + 0.125) + 3) / 4
        return np.min([new, 1])

    if v == 0:
        vprime = 0
    elif v > 0:
        if v < 2:
            vprime = adjusted(v)
        else:
            vprime = np.log2(v)
    elif v < 0:
        v = np.abs(v)
        if v < 2:
            vprime = -adjusted(v)
        else:
            vprime = -np.log2(v)
    else:
        raise ValueError('found value not considered')

    return vprime

########################################################################################################################################

def ttest_viz(df1, df2, title):
    
    #T-test
    t_statistic, p_values = stats.ttest_ind(df1, df2, axis = 0)
    diff = np.mean(df1, axis = 0) - np.mean(df2, axis = 0)
    p_values[np.isnan(p_values)] = 1.0

    reject, q_values = multitest.fdrcorrection(p_values)
    q_values = np.clip(q_values, a_min = 10**(-15), a_max = 1)
    diff = np.clip(diff, a_min = -7, a_max = diff.max())
    
    t_results = pd.DataFrame({
    'p_value': p_values,
    'q_value': q_values,
    'diff': diff
    })
    t_results['sign'] = 'NO SIGNIFICANCE'
    for idx, row in t_results.iterrows():
        if row['q_value'] < 0.05 and row['diff'] > 1:
            t_results.loc[idx, 'sign'] = 'POSITIVE'
        elif row['q_value'] < 0.05 and row['diff'] < -1:
            t_results.loc[idx, 'sign'] = 'NEGATIVE'
    ts_results = t_results[t_results['sign'] != 'NO SIGNIFICANCE']

    #Visualization
    plt.figure(figsize = (10, 8))
    t_colors = {"NO SIGNIFICANCE":"#D2D2D2", "POSITIVE":"#FF2926", "NEGATIVE":"#2183FF"}
    sns.scatterplot(x = t_results['diff'], y = -np.log10(t_results['q_value']), hue = t_results['sign'], palette = t_colors, 
                    alpha = 0.7, size = t_results['sign'], sizes=[40, 100, 100])

    
    plt.title(title)
    plt.ylabel('Significance(-log10(q-value))')
    plt.xlabel('Difference')
    plt.axhline(-np.log10(0.05), color = 'k', linestyle = '--', linewidth = 1, label = 'THRESHOLD')
    plt.axvline(1, color = 'k', linestyle = '--', linewidth = 1)
    plt.axvline(-1, color = 'k', linestyle = '--', linewidth = 1)
    legend_patches = [plt.Line2D([0], [0], marker = 'o', color = 'w', markerfacecolor = color, markersize = 10)
                  for color in t_colors.values()]
    plt.legend(legend_patches, t_colors.keys(), loc = 'best', title = "Difference")
    plt.xlim(-7.2, 7.2)
    plt.grid(True)
    plt.show()
    
    return t_results, ts_results

########################################################################################################################################

def hgtest_viz(subsystems_df, ts_results):
    
    #Hypergeometric test
    ts_subsystems = subsystems_df[subsystems_df.index.isin(ts_results.index)]
    
    ss_counts = subsystems_df['Subsystem'].value_counts()
    m_counts = ts_subsystems['Subsystem'].value_counts()
    
    N = len(subsystems_df)
    n = len(ts_subsystems)
    
    results = []
    for subsystem in ts_subsystems['Subsystem'].unique():
        K = ss_counts.get(subsystem, 0)
        k = m_counts.get(subsystem, 0)
        p_value = hypergeom.sf(k - 1, N, K, n)
        results.append({
            'Subsystem': subsystem,
            'Count': k,
            'Ratio': k/K,
            'p-value': p_value
        })
    ht_results = pd.DataFrame(results)
    reject, q_values = multitest.fdrcorrection(ht_results['p-value'])
    ht_results['q-value'] = q_values
    hts_results = ht_results[ht_results['q-value'] < 0.05]
    hts_results = hts_results.sort_values(by = 'Ratio', ascending = False)
    
    return ht_results, hts_results
    