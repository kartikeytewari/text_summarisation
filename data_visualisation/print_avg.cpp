#include <bits/stdc++.h>
#define line_count 10100
#define local_file_count 101
using namespace std;

struct rouge
{
    long double precision;
    long double recall;
    long double f1_score;
};

struct data_point
{
    long double local_file_weight;
    long double local_file;
    rouge rouge_1;
    rouge rouge_2;
    rouge rouge_l;
};

struct f1_rouge
{
    long double rouge_1;
    long double rouge_2;
    long double rouge_l;
};

int main()
{
    vector<data_point> arr(line_count);
    for (int i=0;i<=line_count-1;i++)
    {
        cin >> arr[i].local_file_weight >> arr[i].local_file;
        cin  >> arr[i].rouge_1.f1_score >> arr[i].rouge_1.precision >> arr[i].rouge_1.recall;
        cin  >> arr[i].rouge_2.f1_score >> arr[i].rouge_2.precision >> arr[i].rouge_2.recall;
        cin  >> arr[i].rouge_l.f1_score >> arr[i].rouge_l.precision >> arr[i].rouge_l.recall;
    }

    // hash map of local_weight and average f1-scores (rouge-1, rouge-2 and rouge-l)
    map<int, f1_rouge> f1_avg;
    for (int i=0;i<=line_count-1;i++)
    {
        f1_avg[arr[i].local_file_weight].rouge_1 += arr[i].rouge_1.f1_score;
        f1_avg[arr[i].local_file_weight].rouge_2 += arr[i].rouge_2.f1_score;
        f1_avg[arr[i].local_file_weight].rouge_l += arr[i].rouge_l.f1_score;
    }

    for (auto it=f1_avg.begin();it!=f1_avg.end();it++)
    {
        it->second.rouge_1 /= local_file_count;
        it->second.rouge_2 /= local_file_count;
        it->second.rouge_l /= local_file_count;

        it->second.rouge_1 *= 100;
        it->second.rouge_2 *= 100;
        it->second.rouge_l *= 100;
    }

    cout << "local_file_weight, rouge_1_f1, rouge_2_f1, rouge_l_f1" << endl;
    for (auto it=f1_avg.begin();it!=f1_avg.end();it++)
    {
        cout << it->first << "," << it->second.rouge_1 << "," << it->second.rouge_2 << "," << it->second.rouge_l << endl;
    }

    return 0;
}