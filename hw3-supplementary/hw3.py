from scipy.linalg import eigh
import numpy as np
import matplotlib.pyplot as plt

def load_and_center_dataset(filename):
    data = np.load(filename)
    data = data - np.mean(data, axis=0)
    return data

def get_covariance(dataset):
    return (1/(len(dataset) -1)) *np.dot(np.transpose(dataset), dataset)

def get_eig(S, m):
    #eigh <- 고유값과 고유벡터를 계산하기 위해 사용 (오름차순으로 반환하며, 대칭 행렬의 경우에는 특히 유용)
    eigenvalues, eigenvectors = eigh(S,subset_by_index = [len(S) - m, len(S) - 1]) #[len(S) - m, len(S) - 1(인덱스라 한개빼줘야 맨 마지막 값)] = largest eigenvalue (m개)
    #get the eigenvalues in decreasing order
    eigenvalues = np.flip(eigenvalues) #np.flip() -> 배열을 역순으로 정리
    eigenvalues = np.diag(eigenvalues) #np.diag() ->  k번째 열부터 있는 대각선의 값들을 1차원 array로 반환
    eigenvectors = np.fliplr(eigenvectors) #np.fliplr() -> 배열을 좌우반전으로 정리
    return eigenvalues, eigenvectors

def get_eig_prop(S, prop):
    #eigh <- 고유값과 고유벡터를 계산하기 위해 사용 (오름차순으로 반환하며, 대칭 행렬의 경우에는 특히 유용)
    eigenvalues, eigenvectors = eigh(S)
    for i in range(len(eigenvalues)):
        if eigenvalues[i]/sum(eigenvalues) > prop:
            m = i
            break
    eigenvalues, eigenvectors = eigh(S, subset_by_index = [m, len(S)-1])
    eigenvalues = np.flip(eigenvalues) #np.flip() -> 배열을 역순으로 정리
    eigenvalues = np.diag(eigenvalues) #np.diag() ->  k번째 열부터 있는 대각선의 값들을 1차원 array로 반환
    eigenvectors = np.fliplr(eigenvectors) #np.fliplr() -> 배열을 좌우반전으로 정리
    return eigenvalues, eigenvectors

def project_image(image, U):
    transpose = np.transpose(U)
    ans = np.empty(0)
    for i in range(len(U)):
        projection = np.dot(np.dot(transpose, image),U[i])
        ans = np.append(ans, projection)
    return ans

def display_image(orig, proj):
    #Reshape the images to be 32 × 32
    orig = np.rot90(np.reshape(orig,(32,32)), axes = (1, 0))
    proj = np.rot90(np.reshape(proj,(32,32)), axes = (1, 0))
    fig, (ax1, ax2) = plt.subplots(figsize=(9, 3), ncols=2)
    ax1.set_title("Original")
    ax2.set_title("Projection")
    show1 = ax1.imshow(orig,aspect = 'equal')
    show2 = ax2.imshow(proj,aspect = 'equal')
    fig.colorbar(show1, ax=ax1)
    fig.colorbar(show2, ax=ax2)
    plt.show()
    return fig, ax1, ax2
