import matplotlib.pyplot as plt
from sklearn import cluster

def elbow_diagram(norm_inertia, x, log=False, filename=None, title=None):
    """Plots elbow diagram."""
    fig, ax = plt.subplots(figsize=(4,3))
    plt.plot(x, norm_inertia)
    ax.set_xlabel('Number of Clusters (k)')
    if title:
        ax.set_title(title)
    if log:
        ax.set_ylabel('Inertia (log)')
        ax.set_yscale('log')
    else:
        ax.set_ylabel('Inertia')
    plt.tight_layout()
    if filename:
        plt.savefig(filename)
    plt.show()

def run_kmeans(k, v, n_dim, n_init):
    """Function to execute $k$-means

    Note that spectral clustering uses two parameters, $n_{eig}$ eigenvectors to fit $k$ 
    clusters.  Typically these two values are equal, but adding dimensions makes the elbow 
    diagram unstable, so $n_{eig}$ was selected that gives good definition between cluster 
    inertia values.
    """
    v_k = v[:, :n_dim]
    kmeans = cluster.KMeans(n_clusters=k, n_init=n_init, random_state=42).fit(v_k)
    return kmeans
