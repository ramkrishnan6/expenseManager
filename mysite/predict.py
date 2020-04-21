import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import chi2
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC


def predict(transaction):
    df = pd.read_csv('~/project/dataset.csv')
    df = df[['Category', 'Description']]
    df = df[pd.notnull(df['Description'])]
    df['category_id'] = df['Category'].factorize()[0]
    category_id_df = df[['Category', 'category_id']].drop_duplicates().sort_values('category_id')
    category_to_id = dict(category_id_df.values)
    tfidf = TfidfVectorizer(
        sublinear_tf=True,
        min_df=2,
        norm='l2',
        encoding='latin-1',
        ngram_range=(1, 2),
        stop_words='english'
    )
    features = tfidf.fit_transform(df.Description).toarray()
    labels = df.category_id

    for Category, category_id in sorted(category_to_id.items()):
        features_chi2 = chi2(features, labels == category_id)

    X_train, X_test, y_train, y_test = train_test_split(df['Description'], df['Category'], random_state=0)
    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(X_train)
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
    clf = LinearSVC().fit(X_train_tfidf, y_train)

    return clf.predict(count_vect.transform([transaction]))