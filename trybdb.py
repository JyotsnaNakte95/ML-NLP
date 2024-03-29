import re
from gensim import models, corpora
from nltk import word_tokenize
from nltk.corpus import stopwords

from nltk.corpus import brown
import nltk
nltk.download('brown')

NUM_TOPICS = 20
STOPWORDS = stopwords.words( 'english' )


def clean_text(text):
    tokenized_text = word_tokenize( text.lower() )
    cleaned_text = [t for t in tokenized_text if t not in STOPWORDS and re.match( '[a-zA-Z\-][a-zA-Z\-]{2,}', t )]
    return cleaned_text

def main():
    data = []


    for fileid in brown.fileids():
        document = ' '.join( brown.words( fileid ) )
        data.append( document )

    NO_DOCUMENTS = len( data )
    print( NO_DOCUMENTS )
    print( data[:5] )
# For gensim we need to tokenize the data and filter out stopwords
    tokenized_data = []
    for text in data:
        tokenized_data.append( clean_text( text ) )

# Build a Dictionary - association word to numeric id
    dictionary = corpora.Dictionary( tokenized_data )

# Transform the collection of texts to a numerical form
    corpus = [dictionary.doc2bow( text ) for text in tokenized_data]

# Have a look at how the 20th document looks like: [(word_id, count), ...]
    print( corpus[20] )
# [(12, 3), (14, 1), (21, 1), (25, 5), (30, 2), (31, 5), (33, 1), (42, 1), (43, 2),  ...

# Build the LDA model
    lda_model = models.LdaModel( corpus=corpus, num_topics=NUM_TOPICS, id2word=dictionary )

# Build the LSI model
    lsi_model = models.LsiModel( corpus=corpus, num_topics=NUM_TOPICS, id2word=dictionary )


    print( "LDA Model:" )

    for idx in range( NUM_TOPICS ):
    # Print the first 10 most representative topics
        print( "Topic #%s:" % idx, lda_model.print_topic( idx, 10 ) )

    print( "=" * 20 )

    print( "LSI Model:" )

    for idx in range( NUM_TOPICS ):
    # Print the first 10 most representative topics
        print( "Topic #%s:" % idx, lsi_model.print_topic( idx, 10 ) )

    print( "=" * 20 )

    text = open('17170-0.txt', 'r').read()
    bow = dictionary.doc2bow( clean_text( text ) )

    print( lsi_model[bow] )
    # [(0, 0.091615426138426506), (1, -0.0085557463300508351), (2, 0.016744863677828108), (3, 0.040508186718598529), (4, 0.014201267714185898), (5, -0.012208538275305329), (6, 0.031254053085582149), (7, 0.017529584659403553), (8, 0.056957633371540077),
    #(9, 0.025989149894888153)]

    print( lda_model[bow] )

if __name__ == '__main__':
    main()