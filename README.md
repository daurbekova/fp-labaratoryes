Для выполнения задачи подсчета количества объектов (квадратов, звезд, кругов, сердечек и треугольников) с использованием **MapReduce** в **Cloudera** через VirtualBox, следуйте этим шагам. Реализация будет на **Java**.

### Шаг 0: Подготовка данных в HDFS

1. Подготовьте набор данных, содержащий объекты, например:

   ```
   square
   star
   circle
   heart
   triangle
   square
   star
   ```

2. Загрузите эти данные в HDFS, используя следующие команды:

   ```bash
   hdfs dfs -mkdir /user/hadoop/shapes_data
   hdfs dfs -put /path/to/shapes_data.txt /user/hadoop/shapes_data
   ```

   Разделите данные на 4 части и загрузите их как отдельные файлы в HDFS.

### Шаг 1: Map (Сопоставление данных)

Создайте MapReduce программу на **Java** для выполнения подсчета. Программа будет содержать Mapper и Reducer классы.

#### Mapper (Java)

Этот класс будет получать строки и генерировать пары "ключ-значение", где ключ — это название объекта (фигура), а значение — единица.

```java
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

public class ShapeMapper extends Mapper<Object, Text, Text, IntWritable> {

    private final static IntWritable one = new IntWritable(1);
    private Text shape = new Text();

    public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
        String shapeStr = value.toString();
        shape.set(shapeStr);
        context.write(shape, one);
    }
}
```

### Шаг 2: Сортировка и перемешивание (Shuffle and Sort)

Hadoop автоматически сортирует и группирует данные по ключам после выполнения Mapper. Это позволяет Reducer получать сгруппированные данные для обработки.

### Шаг 3: Reduce (Подсчет значений)

Reducer будет суммировать значения для каждого ключа, чтобы вычислить количество каждой фигуры.

#### Reducer (Java)

```java
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

public class ShapeReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

    private IntWritable result = new IntWritable();

    public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
        int sum = 0;
        for (IntWritable val : values) {
            sum += val.get();
        }
        result.set(sum);
        context.write(key, result);
    }
}
```

### Main Class (Запуск Job)

Создайте основной класс, который будет управлять запуском MapReduce Job:

```java
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class ShapeCount {

    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "shape count");

        job.setJarByClass(ShapeCount.class);
        job.setMapperClass(ShapeMapper.class);
        job.setCombinerClass(ShapeReducer.class);  // Optional, acts as a local reducer
        job.setReducerClass(ShapeReducer.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
```

### Компиляция и запуск MapReduce Job

1. **Компилируйте** программу:

   Перейдите в директорию с вашим проектом и выполните команду для компиляции:

   ```bash
   javac -classpath `hadoop classpath` -d . ShapeMapper.java ShapeReducer.java ShapeCount.java
   jar cf shape_count.jar *.class
   ```

2. **Запустите MapReduce Job**:

   Теперь, когда у вас есть скомпилированный JAR-файл, запустите его в вашем Hadoop-кластере:

   ```bash
   hadoop jar shape_count.jar ShapeCount /user/hadoop/shapes_data /user/hadoop/output_shapes
   ```

### Проверка результата

После успешного выполнения MapReduce задания, результат будет сохранен в выходной директории `/user/hadoop/output_shapes`. Чтобы посмотреть результат, выполните команду:

```bash
hdfs dfs -cat /user/hadoop/output_shapes/part-r-00000
```

Результат будет выглядеть так:

```
circle    2
heart     1
square    2
star      2
triangle  1
```

### Заключение

Этот пример демонстрирует, как с помощью MapReduce на Java можно подсчитывать количество различных объектов в наборе данных. MapReduce автоматически выполняет распределенную обработку данных на нескольких узлах Hadoop-кластера, что ускоряет процесс для больших объемов данных.
















package mapReduce;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
public class ShapeCount {
public static void main(String[] args) throws Exception { Configuration conf new Configuration(); Job job Job.getInstance(conf, "shape count");
job.setJarByClass (ShapeCount.class); job.setMapperClass (ShapeMapper.class); job.setCombinerClass (ShapeReducer.class); job.setReducerClass (ShapeReducer.class);
job.setOutputKeyClass (Text.class); job.setOutputValueClass (IntWritable.class);
FileInputFormat.addInputPath(job, new Path(args[0])); FileOutputFormat.setOutputPath(job, new Path(args[1])); //
//
путь
Выходной
Входной
путь
System.exit(job.waitForCompletion(true) ? 0:1);
}
}
