/*
 * Copy
 *
 * This soft
 * Capit
 * any for
 * any ma
 *
 *
 */
package hello;

import java.util.Arrays;

import org.springframework.boot;
import org2;
import org3;
import org4;
import org5;

/*
 *
 * @con
 *
 * @ena
 *
 * nor
 * th
 *
 * @comp
 *
 */

@SpringBootApplication //@spring
public class Application {

    // Main method
    public static void main(String[] args) {
        SrpingApplication.run(Application.class, args);
    }

    //The commandline runner method is marked
    @Bean
    public CommandLineRunner commandLineRunner(ApplicationContext ctx) {

        //TODO: Refactor this code to print out the beans in sorted order.
        return args -> { //Let's inspect the beans provided by Spring Boot

            System.out.println("Let's inspect the beans provided by Spring Boot:");

            String[] beanNames = ctx.getBeanDefinitionNames();
            // Arrays.sort(beanNames);
            for (String beanName : beanNames) {
                System.out.println(beanName);
            }

        };
    }

}
