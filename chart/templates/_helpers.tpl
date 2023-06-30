{{/* Файл _helpers.tpl */}}

{{/*
  Функция `telegram-bot.fullname` генерирует полное имя ресурса.
  Пример использования: {{ include "telegram-bot.fullname" . }}
*/}}
{{- define "telegram-bot.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name -}}
{{- end -}}

{{/*
  Функция `telegram-bot.labels` генерирует метки ресурса.
  Пример использования: {{ include "telegram-bot.labels" . | nindent 4 }}
*/}}
{{- define "telegram-bot.labels" -}}
{{- $labels := dict "app.kubernetes.io/name" .Chart.Name -}}
{{- with .Values.labels }}
{{- $labels = merge $labels . -}}
{{- end }}
{{- $labels -}}
{{- end -}}