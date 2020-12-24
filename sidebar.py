import streamlit as st
import random
from utils.count_files import num_images

class SideBar():

    def __init__(self) -> None:

        self.num_images = num_images()

        self.title = "基于视觉问答的注意力机制可视化系统：VQA Attention Visualize System"
        self.model_name = None
        self.question = None
        self.image_idx = None

        self._title()
        self._model()
        self._question()
        self._image()

        self._show_images()

        # self._show_author()
    
    def _title(self):
        st.sidebar.title(self.title)

    def _model(self):

        st.sidebar.markdown('## 选择模型')

        self.model_name = st.sidebar.selectbox(
            label = '请选择使用的VQA模型',
            options = [
                'MFB: Multi-modal Factorized Bilinear Pooling with Co-Attention Learning',
                # 'MCAN: Deep Modular Co-Attention Networks'
            ],
            index = 0,
            key = 'model_name'
        )

        self._fix_model_name(self.model_name)
    
    def _question(self):
        st.sidebar.markdown('## 输入问题')

        self.question = st.sidebar.text_input(
            label = '请用英文输入问题：',
            value= 'What is the colour of the hat?',  
            key= 'question'
        )

    
    def _image(self):

        st.sidebar.markdown('## 选择图像')

        self.image_idx = st.sidebar.number_input(
            label='请输入或选择图像序号：（目前放了1056张图像，输入-1可以随机展示6张图像）', 
            min_value=-1, max_value=self.num_images, value=1, step=1,
            format='%d'
        )

        if (self.image_idx == -1):
            self.image_idx = None
    
    def _show_images(self):

        if self.image_idx is None:
            
            # choose 6 random images
            show_idxs = random.sample(list(range(self.num_images)), 6)

            for idx in show_idxs:

                st.sidebar.image(f'assets/images/{idx}.jpg',use_column_width=True,caption=idx)
            
        else:
            st.sidebar.image(f'assets/images/{self.image_idx}.jpg',use_column_width=True,caption=self.image_idx)


    def _fix_model_name(self, model_name):

        if ('MFB' in model_name):
            self.model_name = 'mfb'
        
        elif ('MCAN' in model_name):
            self.model_name = 'mcan'
        
        else:
            raise NotImplementedError

    def _show_author(self):

        st.sidebar.markdown(
            '## Future releases'
        )

        st.sidebar.info(
            "Version 2 of this is already underway with -  \n • custom image uploads  \n • many more models!  \n "
            "To stay tuned for future releases, follow me on Twitter.  \n"
            "Please consider starring this repo if you like it!"
        )

        cols = st.sidebar.beta_columns((3,4))

        with cols[0]:
            st.components.v1.iframe(src="https://ghbtns.com/github-btn.html?user=apugoneappu&repo=ask_me_anything&type=star&count=true&size=large",
            height=30)

        with cols[1]:
            st.components.v1.iframe(src="https://platform.twitter.com/widgets/follow_button.html?screen_name=apoorve_singhal&show_screen_name=true&show_count=false&size=l",
            height=30)
        
        st.sidebar.markdown(
            '## About me'
        )
        st.sidebar.info(
            "Hi, I'm Apoorve. I like to explain the working of my networks with simple visualisations.  \n "
            "Please visit [apoorvesinghal.com](https://www.apoorvesinghal.com) if you wish to know more about me."
        )
