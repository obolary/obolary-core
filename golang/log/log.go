package log

import (
	"fmt"
	"os"
	"runtime"
	"strings"
	"time"
)

type Log struct {
	Level     string
	Timestamp time.Time
	Process   string
	Function  string
	File      string
	Line      int
}

func NewLog(level string, offset int) *Log {
	var log Log
	log.Level = level
	log.Timestamp = time.Now().UTC()
	if config.PodName != "" {
		log.Process = config.PodName
	} else {
		log.Process = os.Args[0]
	}
	pc, file, line, _ := runtime.Caller(offset + 2)
	log.File = log.File[strings.LastIndex(file, "/")+1:]
	log.Line = line
	log.Function = runtime.FuncForPC(pc).Name()
	log.Function = log.Function[strings.LastIndex(log.Function, "/")+1:]
	return &log
}

func (l *Log) Emit(template string, args ...interface{}) {
	message := fmt.Sprintf(template, args...)
	fmt.Printf("%s | %s | %s | %s:%d | %s | %s\n", l.Level, l.Timestamp, l.Process, l.File, l.Line, l.Function, message)
}

func Trace(template string, args ...interface{}) {
	if config.TraceEnabled {
		NewLog("TRACE", 1).Emit(template, args...)
	}
}

func Debug(template string, args ...interface{}) {
	if config.DebugEnabled {
		NewLog("DEBUG", 1).Emit(template, args...)
	}
}

func Info(template string, args ...interface{}) {
	NewLog("INFO", 1).Emit(template, args...)
}

func Alarm(template string, args ...interface{}) {
	NewLog("ALARM", 1).Emit(template, args...)
}

func Event(template string, args ...interface{}) {
	NewLog("EVENT", 1).Emit(template, args...)
}
