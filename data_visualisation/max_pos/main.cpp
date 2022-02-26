#include <bits/stdc++.h>
using namespace std;

bool compare (pair<long double,string> a, pair<long double,string> b)
{
    return a.first<b.first;
}

void display_max (vector<vector<pair<long double,string>>> arr, int metric_index, string metric_name)
{
    int line_count=(int)arr[0].size();
    sort(arr[metric_index].begin(), arr[metric_index].end(), compare);
    cout << metric_name << " val= " << arr[metric_index][line_count-1].first << endl;
    cout << metric_name << " index= " << arr[metric_index][line_count-1].second << endl;
}

int main()
{
    long double line_count;
    cin >> line_count;

    vector<vector<pair<long double,string>>> arr(13, vector<pair<long double, string>> (line_count));
    // number of rows -> line_count
    // columns -> metric_count
    for (long double i=0;i<=line_count-1;i++)
    {
        string local_file_weight;
        cin >> local_file_weight;
        for (long double j=0;j<=12;j++)
        {
            cin >> arr[j][i].first;
            arr[j][i].second=local_file_weight;
        }
    }

    display_max (arr, 0, "ROUGE-1 F1-score");
    display_max (arr, 1, "ROUGE-1 Precision");
    display_max (arr, 2, "ROUGE-1 Recall");
    cout << endl;
    display_max (arr, 3, "ROUGE-2 F1-score");
    display_max (arr, 4, "ROUGE-2 Precision");
    display_max (arr, 5, "ROUGE-2 Recall");
    cout << endl;
    display_max (arr, 6, "ROUGE-L F1-score");
    display_max (arr, 7, "ROUGE-L Precision");
    display_max (arr, 8, "ROUGE-L Recall");
    cout << endl;
    display_max (arr, 9, "BLEU-1");
    display_max (arr, 10, "BLEU-2");
    display_max (arr, 11, "BLEU-3");
    display_max (arr, 12, "BLEU-4");


    return 0;
}