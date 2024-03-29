# tom-tat-truyen-generator

<div align="center">
    <img src="https://avatars.githubusercontent.com/u/62142713?v=4" alt="Logo" width="80" height="80" style="
    -moz-border-radius:75px;
    -webkit-border-radius: 75px;
    >
<div align="center">
  <h3 align="center">Tóm tắt truyện Generator</h3>
  <h4 align="center">Tác giả: Phạm Đình Trung Hiếu - hieupham1103</h4>
  <p align="center">
    Một công cụ dùng để tự tạo ra một video kiểu tóm tắt phim
  </p>
</div>

Project có sử dụng thư viện [gTTS](https://github.com/pndurette/gTTS), [Stable Diffusion](stabilityai/stable-diffusion-2-1), [MoviePy](https://zulko.github.io/moviepy/) và một vài thư viện khác bên dưới.

[DEMO](https://www.youtube.com/watch?v=psf5BeDFcWQ)

## Cách dùng

Yêu cầu thư viện:
```
httpx
Pillow
moviepy
requests
gTTS
```

``` bash
./tom-tat-truyen-generator
    /final/
        /chap-1/ # mỗi video ta tạo ra một folder
            /story.txt # nội dung của truyện
        /chap-2/
            /story.txt
        ...
    /bg-music.mp3 #file nhạc nền
    /auth_token.py #file chứa token của huggingface.co
    /main.py #file chương trình
```

Lên [Huggingface](https://huggingface.co/settings/tokens) tạo một tài khoản và một token.

Tạo một file `auth_token.py` và bỏ token vào như mẫu sau:

```
auth_token = "token bỏ đây này"
```

Tạo một folder và file nội dung cho 1 video trong `/final`.
```
#story.txt
“...Dù sao đi nữa, hôm nay cậu nên nghỉ ngơi đi. Nhớ uống nước và lau mồ hôi thường xuyên. Với lại tôi đã để cái chậu nước ở đằng kia rồi, hãy dùng nó để lau khô người.”

Sau bữa ăn, Mahiru đã chuẩn bị một chai nước uống thể thao còn nguyên seal, một cái chậu nước cùng khăn tắm, và một miếng chườm mặt, tất cả đều để trên cái bàn cạnh giường Amane.

Thường thì chẳng ai muốn ở lại nhà một người mình vừa mới gặp cả (lại còn là người khác giới nữa chứ), nên Amane rất biết ơn Mahiru.

Trong khi bị cậu nhìn chằm chằm, cô đang kiểm tra lại xem mọi thứ đã đầy đủ chưa.
...
```

Chạy file main.py

```
python main.py
```

Trong folder của mỗi video sẽ có 2 file

* **output.mp4**: video không có nhạc nền

* **output-audio.mp4**: video có nhạc nền
