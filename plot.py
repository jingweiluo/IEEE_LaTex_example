import matplotlib.pyplot as plt
import numpy as np

# X轴：Demonstration 数量
x = [2, 4, 8, 16]
x_vals = np.array(x)

# 示例数据（BNCI2014001）——6种方法 + std
y_data = {
    "BL": ([56.28, 57.56, 61.88, 65.05], [8.70, 5.74, 5.27, 3.44]),
    "RD":     ([61.28, 61.50, 63.92, 64.69], [0.76, 0.86, 0.85, 0.85]),
    "CTD":     ([61.33, 61.61, 61.56, 66.01], [0.78, 1.05, 0.91, 1.00]),
    "SVM-near":    ([54.20, 50.10, 51.45, 51.50], [0.71, 1.37, 1.02, 1.33]),
    "SVM-far":([62.48, 62.93, 64.75, 67.08], [1.16, 0.81, 0.80, 0.68]),
    "PURE":   ([64.09, 65.60, 66.34, 67.95], [1.02, 0.63, 0.62, 0.52]),
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



# ###################################
# # 画频带分解图
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.signal import butter, filtfilt

# X = np.load('/home/luojingwei/data/Weibo2014/X.npy')
# raw_signal = X[0, 25, :] # index25为C3通道

# # plt.rcParams['font.family'] = 'Serif'
# # plt.rcParams['font.serif'] = ['Times New Roman']

# def bandpass_filter(sig, fs, fmin, fmax, order=4):
#     b, a = butter(order, [fmin / (fs/2), fmax / (fs/2)], btype='band')
#     return filtfilt(b, a, sig)

# # 频带定义
# bands = {
#     'B1 [8-12 Hz]': (8, 12),
#     'B2 [12-16 Hz]': (12, 16),
#     'B3 [16-20 Hz]': (16, 20),
#     'B4 [20-24 Hz]': (20, 24)
# }

# fs = 200
# filtered_signals = []
# for label, (fmin, fmax) in bands.items():
#     filtered = bandpass_filter(raw_signal, fs, fmin, fmax)
#     filtered_signals.append(filtered)

# # 画图
# plt.figure(figsize=(7, 5))
# offset = 0
# colors = ['#49006a', '#253494', '#2c7fb8', '#41b6c4', '#a1dab4']  # 可自定义
# names = ['Raw'] + list(bands.keys())
# signals_to_plot = [raw_signal] + filtered_signals

# for i, (y, name, color) in enumerate(zip(signals_to_plot, names, colors)):
#     plt.plot(y/2 - i*2*np.std(raw_signal), color=color, linewidth=2)
#     plt.text(-20, -i*2*np.std(raw_signal), name, va='center', ha='right', fontsize=12)

# plt.axis('off')
# plt.tight_layout()
# plt.savefig('band_filtered_signals.png', dpi=300, bbox_inches='tight')  # 保存图片
# plt.show()