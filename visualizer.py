from reader import read_file,count_vowels
import matplotlib.pyplot as plt

def vowel_visualizer(file):
    vowels_data = count_vowels(file)
    x = list(vowels_data.keys())
    h = list(vowels_data.values())
    color = ['#89f8ff','#ff8833']
    plt.bar(x,h,color=color)
    plt.savefig('images/vowel_counter.png',bbox_inches='tight')

# calling function
file = 'data/Richardson_Clarissa.txt'
vowel_visualizer(file)


