#include <bits/stdc++.h>
using namespace std;

struct rouge
{
    long double f1_score=0;
    long double precision=0;
    long double recall=0;
};

struct doc_val
{
    rouge rouge_1;
    rouge rouge_2;
    rouge rouge_l;
    long double bleu_1=0;
    long double bleu_2=0;
    long double bleu_3=0;
    long double bleu_4=0;
};

int main()
{
    int document_count, gradient_count;
    cin >> document_count >> gradient_count;

    vector<doc_val> arr(gradient_count);
    int line_count=document_count*gradient_count;
    vector<doc_val> gradient(gradient_count);
    for (int i=0;i<=line_count-1;i++)
    {
        float local_file_weight_index;
        int local_file;
        cin >> local_file_weight_index >> local_file;

        int local_file_weight=(local_file_weight_index*10)-900;

        long double rouge_1_f1_score, rouge_1_precision, rouge_1_recall;
        cin >> rouge_1_f1_score >> rouge_1_precision >> rouge_1_recall;
        gradient[local_file_weight].rouge_1.f1_score+=rouge_1_f1_score;
        gradient[local_file_weight].rouge_1.precision+=rouge_1_precision;
        gradient[local_file_weight].rouge_1.recall+=rouge_1_recall;


        long double rouge_2_f1_score, rouge_2_precision, rouge_2_recall;
        cin >> rouge_2_f1_score >> rouge_2_precision >> rouge_2_recall;
        gradient[local_file_weight].rouge_2.f1_score+=rouge_2_f1_score;
        gradient[local_file_weight].rouge_2.precision+=rouge_2_precision;
        gradient[local_file_weight].rouge_2.recall+=rouge_2_recall;

        long double rouge_3_f1_score, rouge_3_precision, rouge_3_recall;
        cin >> rouge_3_f1_score >> rouge_3_precision >> rouge_3_recall;
        gradient[local_file_weight].rouge_l.f1_score+=rouge_3_f1_score;
        gradient[local_file_weight].rouge_l.precision+=rouge_3_precision;
        gradient[local_file_weight].rouge_l.recall+=rouge_3_recall;

        long double bleu_1, bleu_2, bleu_3, bleu_4;
        cin >> bleu_1 >> bleu_2 >> bleu_3 >> bleu_4;
        gradient[local_file_weight].bleu_1+=bleu_1;
        gradient[local_file_weight].bleu_2+=bleu_2;
        gradient[local_file_weight].bleu_3+=bleu_3;
        gradient[local_file_weight].bleu_4+=bleu_4;
    }

    for (int i=0;i<=gradient_count-1;i++)
    {
        gradient[i].rouge_1.f1_score/=document_count;
        gradient[i].rouge_1.precision/=document_count;
        gradient[i].rouge_1.recall/=document_count;

        gradient[i].rouge_2.f1_score/=document_count;
        gradient[i].rouge_2.precision/=document_count;
        gradient[i].rouge_2.recall/=document_count;

        gradient[i].rouge_l.f1_score/=document_count;
        gradient[i].rouge_l.precision/=document_count;
        gradient[i].rouge_l.recall/=document_count;

        gradient[i].bleu_1/=document_count;
        gradient[i].bleu_2/=document_count;
        gradient[i].bleu_3/=document_count;
        gradient[i].bleu_4/=document_count;
    }

    cout << "local_file_weight, rouge_1_f1_score, rouge_1_precision, rouge_1_recall, rouge_2_f1_score, rouge_2_precision, rouge_2_recall, rouge_l_f1_score, rouge_l_precision, rouge_l_recall, bleu_1, bleu_2, bleu_3, bleu_4" << endl;
    for (int i=0;i<=gradient_count-1;i++)
    {
        long double local_file_weight=((long double)i/10)+90.0;
        cout << local_file_weight << ", ";
        cout << gradient[i].rouge_1.f1_score << ", " << gradient[i].rouge_1.precision << ", " << gradient[i].rouge_1.recall << ", ";
        cout << gradient[i].rouge_2.f1_score << ", " << gradient[i].rouge_2.precision << ", " << gradient[i].rouge_2.recall << ", ";
        cout << gradient[i].rouge_l.f1_score << ", " << gradient[i].rouge_l.precision << ", " << gradient[i].rouge_l.recall << ", ";
        cout << gradient[i].bleu_1 << ", " << gradient[i].bleu_2 << ", " << gradient[i].bleu_3 << ", " << gradient[i].bleu_4 << endl;
    }

    return 0;
}