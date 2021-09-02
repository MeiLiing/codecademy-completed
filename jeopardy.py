import pandas as pd
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('jeopardy.csv')
df.columns = ['show_number', 'air_date', 'round', 'category', 'value', 'question', 'answer']
# Change the values in the 'value' column to floats
df['value'] = df.apply(lambda x: float(x.value.strip('$').replace(',','')) if x.value != 'None' else 0, axis = 1)

# This function returns a filtered dataframe of the questions containing the given keywords.
def search_questions(dataframe, words_list):
  question_indexes = []
  for i in range(len(df)):
    are_in = 0
    for word in words_list:
      if word.lower() in dataframe.iloc[i]['question'].lower():
        are_in += 1
      if are_in == len(words_list):
        question_indexes.append(i)
  return df.iloc[question_indexes]

# Function test:
words = ['King','England']
# print(search_questions(df, words))
# returns a dataframe of 152 questions

# Count the number of unique answers in a dataframe
def count_unique_answer(dataframe=df):
  return dataframe.answer.value_counts()
# print(count_unique_answer(search_questions(df, words)))

value_of_a_king = search_questions(df,['King']).value.mean()
# print(value_of_a_king)

round_category = df.groupby(['round','category']).answer.count().reset_index()
round_category_pivot = round_category.pivot(index='category', columns='round', values='answer').reset_index()
print(round_category_pivot)
print(round_category_pivot.columns)
print(round_category_pivot[round_category_pivot.category == 'LITERATURE'])
