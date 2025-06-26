<p align="center">
  <a href="https://www.uit.edu.vn/"><img src="https://www.uit.edu.vn/sites/vi/files/banner.png"></a>
<h1 align="center"><b>CS431.P22</b></h1>

## Giới thiệu
* Tên môn học: CÁC KỸ THUẬT HỌC SÂU VÀ ỨNG DỤNG
* Mã lớp: CS431.P22
* Năm học: Học kỳ 6 ( Học kỳ 2 - 2024-2025)

### Giảng viên
* TS.Nguyễn Vinh Tiệp

### Thành viên nhóm

| STT | Họ và tên | MSSV | Email | Github |
| :---: | --- | --- | --- | --- |
| 1 | Nguyễn Duy Thắng | 22521333 | 22521333@gm.uit.edu.vn | [github](https://github.com/DyThen-Kumo) |

### Tóm tắt
Ngôn ngữ ký hiệu (Sign Language) là công cụ giao tiếp quan trọng đối với cộng đồng người khiếm thính và người câm, trong đó American Sign Language (ASL) là một trong những hệ thống ngôn ngữ được sử dụng rộng rãi trên thế giới (chủ yếu sẽ ở Hoa Kỳ và nhiều nơi ở Canada). 

Trong lĩnh vực thị giác máy tính, các mô hình học sâu hiện đại như ResNet, EfficientNet hay Transformer-based models đã đạt độ chính xác cao trong bài toán phân loại ảnh, trong đó có nhận diện ASL. Tuy nhiên, các mô hình này thường có số lượng tham số lớn và đòi hỏi tài nguyên tính toán cao, gây khó khăn trong việc triển khai trên thiết bị di động hoặc nhúng. Ngược lại, dòng mô hình MobileNet được thiết kế đặc biệt cho môi trường tài nguyên hạn chế, như điện thoại thông minh, IoT, hoặc hệ thống nhúng. 

Đề tài “Efficiency of MobileNet model families for ASL Gesture Classification” nhằm phân tích, so sánh khả năng cân bằng giữa độ chính xác và hiệu năng của ba mô hình tiêu biểu: MobileNetV2, MobileNetV3-Small và MobileNetV4-Conv-Small. Chi tiết trong [file](submit/report.pdf)

## Bài toán
Xây dựng một hệ thống phân loại cử chỉ tay tĩnh trong ngôn ngữ ký hiệu Mỹ (ASL), sử dụng hình ảnh RGB đầu vào, với yêu cầu chỉ nhận diện các ảnh có chứa bàn tay. Hệ thống cần phân loại ảnh đầu vào thành một trong 28 lớp ASL, bao gồm 26 chữ cái (A–Z) và hai ký hiệu chức năng (del, space). Các ảnh không có bàn tay sẽ bị loại bỏ khỏi bài toán nhằm đảm bảo tính nhất quán và tính khả thi trong việc nhận dạng bằng hình ảnh cử chỉ tay.

## Demo
[ASL Getsure Demo](https://www.youtube.com/watch?v=AU8EJxgciBo)

## Reference
[1] Diane Brentari. A Prosodic Model of Sign Language Phonology. MIT Press, 1998.

[2] Navneet Dalal and Bill Triggs. “Histograms of oriented gradients for human detection”. inProceedings of
the IEEE Conference on Computer Vision and Pattern Recognition: IEEE. 2005, pages 886–893.

[3] Alexey Dosovitskiy andothers. “An Image is Worth 16x16 Words: Transformers for Image Recognition
at Scale”. inInternational Conference on Learning Representations (ICLR): 2021. url: https://arxiv.
org/abs/2010.11929.

[4] Grassknoted. ASL Alphabet. https : / / www . kaggle . com / datasets / grassknoted / asl - alphabet.
Accessed: 2025-06-13. 2017.

[5] Kaiming He andothers. “Deep Residual Learning for Image Recognition”. in2016 IEEE Conference on
Computer Vision and Pattern Recognition (CVPR): 2016, pages 770–778. doi: 10.1109/CVPR.2016.90.

[6] Andrew Howard andothers. “Searching for MobileNetV3”. inarXiv preprint arXiv:1905.02244 : (2019).
url: https://arxiv.org/abs/1905.02244.

[7] Andrew G. Howard andothers. “MobileNets: Efficient Convolutional Neural Networks for Mobile Vision
Applications”. inarXiv preprint arXiv:1704.04861 : 2017. url: https://arxiv.org/abs/1704.04861.

[8] Jie Hu, Li Shen and Gang Sun. “Squeeze-and-Excitation Networks”. inProceedings of the IEEE Conference
on Computer Vision and Pattern Recognition (CVPR): 2018, pages 7132–7141.

[9] Alex Krizhevsky, Ilya Sutskever and Geoffrey E Hinton. “ImageNet classification with deep convolutional
neural networks”. inAdvances in Neural Information Processing Systems : volume 25. 2012.

[10] Yann LeCun andothers. “Gradient-based learning applied to document recognition”. inProceedings of
the IEEE: 86.11 (1998), pages 2278–2324.

[11] David G Lowe. “Distinctive image features from scale-invariant keypoints”. inInternational Journal of
Computer Vision: volume 60. 2. 2004, pages 91–110.

[12] National Association of the Deaf. What is American Sign Language? Truy cập ngày 10 tháng 6 năm 2025.
2022. url: https://www.nad.org/resources/american-sign-language/what-is-american-signlanguage/.

[13] David M. W. Powers. “Evaluation: from precision, recall and F-measure to ROC, informedness, markedness
and correlation”. inJournal of Machine Learning Technologies: 2.1 (2011), pages 37–63.

[14] Danfeng Qin andothers. “MobileNetV4: Universal Models for the Mobile Ecosystem”. inarXiv preprint
arXiv:2404.10518 : (2024). v2, submitted Apr 16 2024, updated Sep 29 2024. url: https://arxiv.org/
abs/2404.10518.

[15] Mark Sandler andothers. “MobileNetV2: Inverted Residuals and Linear Bottlenecks”. inProceedings of
the IEEE Conference on Computer Vision and Pattern Recognition (CVPR): 2018, pages 4510–4520.
url: https://openaccess.thecvf.com/content_cvpr_2018/html/Sandler_MobileNetV2_Inverted_
Residuals_CVPR_2018_paper.html.

[16] Karen Simonyan and Andrew Zisserman. “Very deep convolutional networks for large-scale image recognition”.
inInternational Conference on Learning Representations: 2015.

[17] William C Stokoe. Sign Language Structure: An Outline of the Visual Communication Systems of the
American Deaf. Department of Anthropology and Linguistics, University of Buffalo, 1960.

[18] Mingxing Tan and Quoc V. Le. “EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks”.
inProceedings of the 36th International Conference on Machine Learning (ICML): byeditorKamalika
Chaudhuri and Ruslan Salakhutdinov. volume 97. Proceedings of Machine Learning Research. PMLR,
june 2019, pages 6105–6114. url: https://proceedings.mlr.press/v97/tan19a.html.

[19] Clayton Valli andothers. Linguistics of American Sign Language: An Introduction. Gallaudet University
Press, 2000.

[20] Ashish Vaswani andothers. “Attention Is All You Need”. inAdvances in Neural Information Processing
Systems (NeurIPS): volume 30. 2017. url: https://papers.nips.cc/paper_files/paper/2017/
hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html.
