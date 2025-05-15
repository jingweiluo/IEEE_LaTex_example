import matplotlib.pyplot as plt
import numpy as np

# X轴：Demonstration 数量
x = [2, 4, 8, 16]
x_vals = np.array(x)

# 示例数据（BNCI2014001）——6种方法 + std
y_data = {
    "BL": ([56.28, 57.56, 61.88, 62.88], [8.70, 5.74, 5.27, 5.27]),
    "RD":     ([61.28, 61.50, 63.92, 64.92], [0.76, 0.86, 0.85, 0.85]),
    "CTD":     ([61.33, 61.61, 61.56, 62.06], [0.78, 1.05, 0.91, 0.91]),
    "SVM-near":    ([54.20, 50.10, 51.45, 51.95], [0.71, 1.37, 1.02, 1.02]),
    "SVM-far":([62.48, 62.93, 64.75, 65.75], [1.16, 0.81, 0.80, 0.80]),
    "PURE":   ([64.09, 65.60, 66.34, 67.34], [1.02, 0.63, 0.62, 0.62]),
}

# 颜色循环（自动分配颜色）
colors = plt.cm.tab10.colors  # 最多10种方法不重复

# 绘图
plt.figure(figsize=(6.5, 5))

for i, (label, (y_vals, std_vals)) in enumerate(y_data.items()):
    y_vals = np.array(y_vals)
    std_vals = np.array(std_vals)

    plt.fill_between(x_vals, y_vals - std_vals, y_vals + std_vals, alpha=0.2, color=colors[i])
    plt.plot(x, y_vals, 'o-', label=label, color=colors[i])

# 坐标轴与图例
plt.title('BNCI2014001')
plt.xlabel('Number of Demonstrations')
plt.ylabel('Accuracy (%)')
plt.xticks(x)
plt.grid(True)
plt.legend(loc='lower right')
plt.tight_layout()

# 导出矢量图和高分辨率 PNG 图
plt.savefig("BNCI2014001_6methods.eps", format='eps', bbox_inches='tight')
plt.savefig("BNCI2014001_6methods.png", format='png', dpi=300, bbox_inches='tight')

plt.show()