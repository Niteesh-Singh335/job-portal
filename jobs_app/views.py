# from django.shortcuts import render
# from jobs_app.models import job
# from django.http import JsonResponse


# def job_list(request):
#     jobs=job.objects.all()
#     data={
#         'jobs':list(jobs.values())
#         }
#     return JsonResponse(data)

# def job_details(request,pk):
#     job_detail=job.objects.get(pk=pk)
#     data={
#         'job_title':job_detail.job_title,
#         'salary':job_detail.salary,
#         'company':job_detail.company,
#         'location':job_detail.location,
#         'description':job_detail.description,
#         'date_and_time':job_detail.date_and_time.isoformat(),
#         'posted_by':job_detail.posted_by.username,
#         'job_type':job_detail.job_type,
#         'current_working':job_detail.current_working
#     }
#     return JsonResponse(data)
