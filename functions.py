# libraries
import numpy as np
from scipy import stats
from statsmodels.stats import multitest
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import hypergeom

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

def ttest_viz(df1, df2, title, filename):
    
    #T-test
    t_statistic, p_values = stats.ttest_ind(df1, df2, axis = 0)
    diff = np.mean(df1, axis = 0) - np.mean(df2, axis = 0)
    p_values[np.isnan(p_values)] = 1.0
    
    reject, q_values = multitest.fdrcorrection(p_values)
    q_values = np.clip(q_values, a_min = 10**(-15), a_max = 1)

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
    t_colors = {"NO SIGNIFICANCE":"#D2D2D2", "POSITIVE":"#FF6462", "NEGATIVE":"#62B8FF"}
    sns.scatterplot(x = t_results['diff'], y = -np.log10(t_results['q_value']), hue = t_results['sign'], palette = t_colors, alpha = 0.7)
    
    plt.title(title)
    plt.ylabel('Significance(-log10(q-value))')
    plt.xlabel('Difference')
    plt.axhline(-np.log10(0.05), color = 'k', linestyle = '--', linewidth = 1, label = 'THRESHOLD')
    plt.axvline(1, color = 'k', linestyle = '--', linewidth = 1)
    plt.axvline(-1, color = 'k', linestyle = '--', linewidth = 1)
    plt.legend(loc = 'best')
    plt.xlim(-8, 8)
    plt.grid(True)
    plt.savefig(filename)
    plt.show()
    
    return t_results, ts_results

########################################################################################################################################

def hgtest_viz(subsystems_df, ts_results, filename):
    
    #Hypergeometric test
    ts_subsystems = subsystems_df[subsystems_df.index.isin(ts_results.index)]
    
    ss_counts = subsystems_df['Subsystem'].value_counts()
    m_counts = ts_subsystems['Subsystem'].value_counts()
    
    rx = len(subsystems_df)
    rx_m = len(ts_subsystems)
    
    results = []
    for subsystem in ts_subsystems['Subsystem'].unique():
        ss_successes = ss_counts.get(subsystem, 0)
        m_successes = m_counts.get(subsystem, 0)
        p_value = hypergeom.sf(m_successes - 1, rx, ss_successes, rx_m)
        results.append({
            'Subsystem': subsystem,
            'Count': m_successes,
            'Ratio': m_successes/ss_successes,
            'p-value': p_value
        })
    ht_results = pd.DataFrame(results)
    reject, q_values = multitest.fdrcorrection(ht_results['p-value'])
    ht_results['q-value'] = q_values
    hts_results = ht_results[ht_results['q-value'] < 0.05]
    hts_results = hts_results.sort_values(by = 'Ratio', ascending = False)

    #Visualization
    plt.figure(figsize = (10, 8))
    sns.scatterplot(data = hts_results, x = 'Ratio', y = 'Subsystem', size = 'Count', sizes = (50, 800), alpha = 0.7,
                hue = -np.log10(hts_results['q-value']), palette = 'viridis_r')
    norm = plt.Normalize(vmin = -np.log10(hts_results['q-value']).min(), vmax = -np.log10(hts_results['q-value']).max())
    sm = plt.cm.ScalarMappable(cmap = 'viridis_r', norm = norm)
    sm.set_array([])
    plt.colorbar(sm, ax = plt.gca(), label = 'Significance(-log10(q-value))')
    
    ax = plt.gca()
    handles, labels = ax.get_legend_handles_labels()
    ax.legend_.remove()
    legend_n = labels.index('Count')
    ax.legend(handles[legend_n:], labels[legend_n:], bbox_to_anchor = (1.5, 0.7), labelspacing = 2, borderpad = 1.5)
    
    plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)
    plt.savefig(filename)
    plt.show()

    return ht_results, hts_results
