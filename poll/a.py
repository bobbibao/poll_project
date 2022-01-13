
import models
poll = models.Poll()
p = poll.objects.all()
print(p.question)