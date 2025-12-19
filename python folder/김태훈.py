import sys
import subprocess

# 필요한 패키지 자동 설치
def install_if_needed(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", package])

for pkg in ["biopython", "matplotlib"]:
    install_if_needed(pkg)

# 실제 코드 시작
from Bio.SeqUtils import gc_fraction
import matplotlib.pyplot as plt

# DNA 서열 샘플
sequences = {
    "Bacteria A": "ATGCGCGATCGATCGATCGT",
    "Bacteria B": "ATATATATATATATATATAT",
    "Bacteria C": "GCGCGCGCGCGCGCGCGCGC",
}

# GC 함량 계산
gc_values = {name: gc_fraction(seq) * 100 for name, seq in sequences.items()}

# 계산 결과 출력
for name, gc_content in gc_values.items():
    print(f"{name}의 GC 함량: {gc_content:.2f}%")

# 그래프 표시
plt.bar(gc_values.keys(), gc_values.values(),
        color=['skyblue', 'lightgreen', 'salmon'])
plt.title("DNA 서열별 GC 함량 비교")
plt.ylabel("GC 함량 (%)")
plt.show()
